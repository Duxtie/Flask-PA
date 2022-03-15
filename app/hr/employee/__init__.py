from flask import Blueprint
from . import models, views  # noqa

occupation_blueprint = Blueprint("employee", __name__)
