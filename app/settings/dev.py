import os.path

DEBUG = True

ADMINISTRATORS = ()

SECRET_KEY = 'development secret'

# For testing collect
COLLECT_STATIC_ROOT = '/tmp/graffathon-static'
COLLECT_STORAGE = 'flask.ext.collect.storage.file'

SQLALCHEMY_DATABASE_URI = 'sqlite:////tmp/graffathon.db'

USERNAME = "admin"
PASSWORD = "password"

# Uploaded media files
MEDIA_FOLDER = '/tmp/graffathon-media'
MEDIA_THUMBNAIL_FOLDER = os.path.join(MEDIA_FOLDER, "cache")
MEDIA_URL = '/media/'
MEDIA_THUMBNAIL_URL = '/media/cache/'

# email server
# TESTING = True
# ADMINS = ['test@localhost.com']

# address from which mails are sent
MAIL_DEFAULT_SENDER = 'graffathon@localhost'

# for testing run SMTP server with
# python -m smtpd -n -c DebuggingServer localhost:1026
# MAIL_DEBUG = True
MAIL_PORT = 1026
