from flask import Blueprint
from . import models, views  # noqa

payroll_blueprint = Blueprint("payroll", __name__)
