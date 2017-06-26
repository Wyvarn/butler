from . import home
from flask import Response, render_template


@home.route("/")
def index():
    return Response("Hello Butler")

