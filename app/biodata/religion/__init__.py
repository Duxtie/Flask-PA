from flask import Blueprint
from . import models, views  # noqa

religion_blueprint = Blueprint("religion", __name__)
