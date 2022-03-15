from flask import Blueprint
from . import models, views  # noqa

country_blueprint = Blueprint("country", __name__)
