from flask import render_template
from app import app


@app.route("/")
@app.route("/index")
def index():
    user = {"username": "Micah"}
    posts = [
        {"author": {"username": "Tila"}, "body": "Beautiful day in NairobiKenya!"},
        {"author": {"username": "Oketch"}, "body": "The paddington anime was so cool!"},
    ]
    return render_template("index.html", title="Home", user=user, posts=posts)
