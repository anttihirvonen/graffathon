# -*- coding: utf-8 -*-
from flask.ext.script import Manager
from flask.ext.collect import Collect

from app import app, db, models

manager = Manager(app)
collect = Collect()
collect.init_app(app)
collect.init_script(manager)


@manager.command
def initialize_database():
    "Drop current database and initialize a new one"
    db.drop_all()
    db.create_all()
    admin = models.Admin(app.config['USERNAME'], app.config['PASSWORD'])
    db.session.add(admin)
    db.session.commit()

    print "Database initialized"


@manager.command
def add_test_user():
    user = models.SignUp("Test User", "test.user@gmail.com", "Aalto-yliopisto TiK", "Vahan.", False, False, True)
    db.session.add(user)
    db.session.commit()

    print "User added"


if __name__ == "__main__":
    manager.run()
