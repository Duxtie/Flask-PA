from flask import Blueprint
from . import models, views, api  # noqa

contact_blueprint = Blueprint("contact", __name__)
