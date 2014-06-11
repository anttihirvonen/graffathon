# -*- coding: utf-8 -*-
from flask.ext.wtf import Form
from wtforms import TextField, PasswordField, TextAreaField, validators
from wtforms.validators import Required, StopValidation, ValidationError
from models import Admin, SignUp
from flask import flash


def validate_email(form, field):
    existing_email = SignUp.query.filter_by(visible=True, email=field.data).first()

    if existing_email:
        raise ValidationError(u'Email already exists')


class SignUpForm(Form):
    name = TextField(u'Nimi', [validators.Required()])
    email = TextField(u'Sähköposti', [validators.Email(), validate_email])
    school = TextField(u'Koulu, koulutusohjelma ja vuosikurssi')
    experience = TextAreaField(u'Kokemus tietokonegrafiikasta ja/tai demoskenestä')

    def __init__(self, *a, **kw):
        Form.__init__(self, *a, **kw)


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
