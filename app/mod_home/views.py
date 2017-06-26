from . import home
from flask import Response


@home.route("/")
def index():
    return Response("Hello Butler")

