from flask import Blueprint

# Import blueprints
# from .payroll import payroll_blueprint
from .client import client_blueprint
from .occupation import occupation_blueprint

# from .salary_plan import salary_plan_blueprint

hr_blueprint = Blueprint("hr", __name__)
