# -*- coding: utf-8 -*-
from flask.ext.sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
from app import db


class SignUp(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    email = db.Column(db.String(80))
    school = db.Column(db.String(80))
    experience = db.Column(db.Text)
    paid = db.Column(db.Boolean)
    confirmed = db.Column(db.Boolean)
    visible = db.Column(db.Boolean)
    created = db.Column(db.DateTime)
    confirmed_at = db.Column(db.DateTime, nullable=True)

    def __init__(self, name, email, school, experience, paid, confirmed, visible, created=None):
        self.name = name
        self.email = email
        self.school = school
        self.experience = experience
        self.paid = paid
        self.confirmed = confirmed
        self.visible = visible
        if created is None:
            created = datetime.utcnow()
        self.created = created
        self.confirmed_at = None

    def __repr__(self):
        return '<SignUp %r>' % self.name


class Admin(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    password = db.Column(db.String(80))

    def __init__(self, username, password):
        self.username = username
        self.set_password(password)

    def __repr__(self):
        return '<Admin %r>' % self.username

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def is_active(self):
        return True

    def is_authenticated(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return unicode(self.id)
