from flask import Blueprint
from . import models, views  # noqa

company_blueprint = Blueprint("company", __name__)
