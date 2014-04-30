from flask import Flask, render_template
from werkzeug.contrib.fixers import ProxyFix


app = Flask(__name__)
app.wsgi_app = ProxyFix(app.wsgi_app)

app.config.from_object('app.settings.common')
app.config.from_envvar('GRAFFATHON_SETTINGS')


@app.route('/')
def index():
    return render_template('index.html')
