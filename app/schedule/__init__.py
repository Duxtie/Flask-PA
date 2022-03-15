from flask import Blueprint

# Import blueprints
from .allergy import allergy_blueprint
from .medication_list import medication_list_blueprint
from .health_maintenance import health_maintenance_blueprint

medical_history_blueprint = Blueprint("medical_history", __name__)
