import os
from flask import Flask, render_template

SECRET_KEY = os.environ['SECRET_KEY']

app = Flask(__name__)
app.secret_key = SECRET_KEY

app.jinja_env.add_extension('jinja2.ext.loopcontrols')
app.config.from_object(__name__)


@app.route('/')
def index():
    return render_template("index.html", title="Home")


@app.route('/ourteam')
def ourteam():
    return render_template("ourteam.html", title="Our Team")


@app.route('/ourorganisation')
def ourorganisation():
    return render_template("ourorganisation.html", title="Our Organisation")


@app.route('/supportus')
def supportus():
    return render_template("supportus.html", title="Support Us")


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    host = "0.0.0.0"
    app.run(host=host, port=port, debug=True)
