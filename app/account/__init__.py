from etas import app
from flask import Blueprint

# Import blueprints
from .contact import contact_blueprint

account_blueprint = Blueprint("account", __name__)

# Register blueprints
# app.register_blueprint(contact_blueprint)
