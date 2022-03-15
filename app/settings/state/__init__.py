from flask import Blueprint
from . import models, views  # noqa

state_blueprint = Blueprint("state", __name__)
