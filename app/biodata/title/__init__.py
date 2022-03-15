from flask import Blueprint
from . import models, views  # noqa

title_blueprint = Blueprint("title", __name__)
