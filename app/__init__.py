# -*- coding: utf-8 -*-
from flask import Flask, render_template, request, redirect, url_for
from werkzeug.contrib.fixers import ProxyFix
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import LoginManager, login_required, login_user, logout_user
from flask.ext.mail import Message, Mail

app = Flask(__name__)
app.wsgi_app = ProxyFix(app.wsgi_app)

app.config.from_object('app.settings.common')
app.config.from_envvar('GRAFFATHON_SETTINGS')

db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = '/login'

mail = Mail(app)
mail.init_app(app)

from models import SignUp, Admin
from forms import SignUpForm, LoginForm
from emails import send_email


# TODO: handling all these static page routes
# manually is stupid. generate url's automatically
# by walking the template directory and doing conversion
# (_ -> -,) for urls and / -> _ for function names.
# eg. /info/test-page -> template: info/test_page.html,
# function name: info_test_page (usable for menus)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/info')
def info():
    return render_template('info/index.html')


@app.route('/info/competitions')
def info_competitions():
    return render_template('info/competitions.html')


@app.route('/info/timetable')
def info_timetable():
    return render_template('info/timetable.html')


@app.route('/info/speakers')
def info_speakers():
    return render_template('info/speakers.html')


@app.route('/info/location')
def info_location():
    return render_template('info/location.html')


@app.route('/info/faq')
def info_faq():
    return render_template('info/faq.html')


@app.route('/team')
def team():
    return render_template('team.html')


@app.route('/in-english')
def in_english():
    return render_template('in_english.html')


@app.route('/signup', methods=['GET', 'POST'])
def signup():
	form = SignUpForm()

	if request.method == 'POST' and form.validate_on_submit():
		signup = SignUp("", "", "", "", False)
		signup.name = form.name.data
		signup.email = form.email.data
		signup.school = form.school.data
		signup.experience = form.experience.data
		db.session.add(signup)
		db.session.commit()

		send_email("Testing", app.config['ADMINS'][0], [form.email.data], "Just testing", "")
		return redirect('/')

	return render_template('signup.html', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
	form = LoginForm()
	if request.method == 'POST' and form.validate_on_submit():
		login_user(form.admin)
		return redirect(request.args.get("next") or url_for('show_participants'))

	return render_template('login.html', form=form)

@app.route('/logout', methods=['GET'])
@login_required
def logout():
	logout_user()
	return redirect('/')

@login_manager.user_loader
def load_user(userid):
	return Admin.query.get(int(userid))

@app.route('/osallistujat')
@login_required
def show_participants():
	signups = SignUp.query.order_by(SignUp.created.asc())
	return render_template('participants.html', signups=signups)
