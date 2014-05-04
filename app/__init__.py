# -*- coding: utf-8 -*-
from flask import Flask, render_template, request, redirect
from werkzeug.contrib.fixers import ProxyFix
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.wsgi_app = ProxyFix(app.wsgi_app)

app.config.from_object('app.settings.common')
app.config.from_envvar('GRAFFATHON_SETTINGS')

db = SQLAlchemy(app)

from models import SignUp
from forms import SignUpForm

db.create_all()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ilmoittautuminen', methods=['GET', 'POST'])
def signup():
	form = SignUpForm()
	signups = SignUp.query.order_by(SignUp.created.desc())

	if request.method == 'POST':
		signup = SignUp("", "", "", "")
		signup.name = form.name.data
		signup.email = form.email.data
		signup.school = form.school.data
		signup.experience = form.experience.data
		db.session.add(signup)
		db.session.commit()
		return redirect('/ilmoittautuminen')

	return render_template('signup.html', form=form, signups=signups)
