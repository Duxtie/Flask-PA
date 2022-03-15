from flask import Blueprint
from . import models, views
dashboard_blueprint = Blueprint("dashboard", __name__)
