from flask import render_template
from app import app
from app.forms import LoginForm


@app.route("/")
@app.route("/index")
@app.route("/login")
def index():
    user = {"username": "Micah"}
    posts = [
        {"author": {"username": "Tila"}, "body": "Beautiful day in NairobiKenya!"},
        {"author": {"username": "Oketch"}, "body": "The paddington anime was so cool!"},
    ]
    return render_template("index.html", title="Home", user=user, posts=posts)


def login():
    form = LoginForm()
    return render_template("login.html", title="Sign in", form=form)
