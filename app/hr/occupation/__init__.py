from flask import Blueprint
from . import models, views  # noqa

occupation_blueprint = Blueprint("occupation", __name__)
