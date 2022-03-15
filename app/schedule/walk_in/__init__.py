from flask import Blueprint
from . import models, views, api  # noqa

walk_in_blueprint = Blueprint("walk_in", __name__)
