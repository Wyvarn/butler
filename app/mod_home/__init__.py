from flask import Blueprint


home = Blueprint(name="home", import_name=__name__, url_prefix="/", static_folder="static",
                 template_folder="templates")

from . import views
