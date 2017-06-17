from . import home
from flask import Response, render_template


@home.route("/")
def index():
    # return "Hello Butler"
    # return Response("Hello Butler")
    return render_template("home.html")

