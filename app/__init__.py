from flask import Flask, render_template


app = Flask(__name__)
app.config.from_object('app.settings.common')
app.config.from_envvar('GRAFFATHON_SETTINGS')


@app.route('/')
def index():
    return render_template('index.html')
