from flask import Blueprint
from . import models, views  # noqa

marital_status_blueprint = Blueprint("marital_status", __name__)