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


if __name__ == "__main__":
    manager.run()
