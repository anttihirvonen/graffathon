DEBUG = True

SECRET_KEY = 'development secret'

# For testing collect
COLLECT_STATIC_ROOT = '/tmp/graffathon-static'
COLLECT_STORAGE = 'flask.ext.collect.storage.file'

SQLALCHEMY_DATABASE_URI = 'sqlite:////tmp/graffathon.db'
