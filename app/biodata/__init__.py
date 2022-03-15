from flask import Blueprint

# Import blueprints
from .gender import gender_blueprint
from .marital_status import marital_status_blueprint
from .religion import religion_blueprint

biodata_blueprint = Blueprint("biodata", __name__)
