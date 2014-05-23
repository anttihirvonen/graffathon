# Production settings
import os

DEBUG = False

# Emails delimited with comma, no spaces!
ADMINISTRATORS = os.environ['ADMINISTRATORS'].split(',')

SECRET_KEY = os.environ['SECRET_KEY']

COLLECT_STATIC_ROOT = os.environ['COLLECT_STATIC_ROOT']
COLLECT_STORAGE = 'flask.ext.collect.storage.file'

SQLALCHEMY_DATABASE_URI = os.environ['SQLALCHEMY_DATABASE_URI']

USERNAME = os.environ['USERNAME']
PASSWORD = os.environ['PASSWORD']

# Mail is sent from localhost,
# so no extra configuration is needed
MAIL_SERVER = 'localhost'
MAIL_DEFAULT_SENDER = 'dot@kapsi.fi'
