from flask import Blueprint
from . import models, views  # noqa

gender_blueprint = Blueprint("gender", __name__)
