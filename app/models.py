from flask.ext.sqlalchemy import SQLAlchemy
from datetime import datetime
from app import db

class SignUp(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(80))
	email = db.Column(db.String(80))
	school = db.Column(db.String(80))
	experience = db.Column(db.Text)
	created = db.Column(db.DateTime)

	def __init__(self, name, email, school, experience, created=None):
		self.name = name
		self.email = email
		self.school = school
		self.experience = experience
		if created == None:
			created = datetime.utcnow()
		self.created = created

	def __repr__(self):
		return '<SignUp %r>' % self.name
