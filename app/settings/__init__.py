from flask import Blueprint

# Import blueprints
from .country import country_blueprint
from .state import state_blueprint

system_setting_blueprint = Blueprint("system_setting", __name__)
