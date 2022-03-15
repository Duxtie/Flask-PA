from flask import Blueprint
from . import models, views  # noqa

salary_plan_blueprint = Blueprint("salary_plan", __name__)
