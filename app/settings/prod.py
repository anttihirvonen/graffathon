# Production settings
import os

DEBUG = False

SECRET_KEY = os.environ['SECRET_KEY']

COLLECT_STATIC_ROOT = os.environ['COLLECT_STATIC_ROOT']
COLLECT_STORAGE = 'flask.ext.collect.storage.file'

SQLALCHEMY_DATABASE_URI = os.environ['SQLALCHEMY_DATABASE_URI']
