# -*- coding: utf-8 -*-
from flask.ext.wtf import Form
from wtforms import TextField, PasswordField, TextAreaField, validators
from wtforms.validators import Required
from models import Admin
from flask import flash

class SignUpForm(Form):
	name = TextField(u'Nimi', [validators.Required()])
	email = TextField(u'Sähköposti', [validators.Email()])
	school = TextField(u'Koulu ja koulutusohjelma')
	experience = TextAreaField(u'Kokemus demoscenestä')

class LoginForm(Form):
	username = TextField(u'Username', [validators.Required()])
	password = PasswordField(u'Password', [validators.Required()])

	def __init__(self, *a, **kw):
		Form.__init__(self, *a, **kw)
		self.admin = None

	def validate_on_submit(self):
		admin = Admin.query.filter_by(username=self.username.data).first()
		if admin is None:
			flash(u'Invalid username')
			return False

		if not admin.check_password(self.password.data):
			flash(u'Invalid password')
			return False

		self.admin = admin
		return True