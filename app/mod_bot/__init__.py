from flask import Blueprint

bot = Blueprint(name="bot", url_prefix="/bot/", static_folder="static",
                template_folder="templates", import_name=__name__)

from . import views
