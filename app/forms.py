# -*- coding: utf-8 -*-
from flask.ext.wtf import Form
from wtforms import TextField, PasswordField, TextAreaField, validators
from wtforms.validators import Required

class SignUpForm(Form):
	name = TextField(u'Nimi', [validators.Required()])
	email = TextField(u'Sähköposti', [validators.Required()])
	school = TextField(u'Koulu ja koulutusohjelma')
	experience = TextAreaField(u'Kokemus demoscenestä')