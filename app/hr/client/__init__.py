from flask import Blueprint
from . import models, views  # noqa

client_blueprint = Blueprint("client", __name__)
