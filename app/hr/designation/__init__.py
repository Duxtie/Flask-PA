from flask import Blueprint
from . import models, views  # noqa

occupation_blueprint = Blueprint("designation", __name__)
