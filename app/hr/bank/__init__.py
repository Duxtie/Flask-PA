from flask import Blueprint
from . import models, views  # noqa

bank_blueprint = Blueprint("bank", __name__)
