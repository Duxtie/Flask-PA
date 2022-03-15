from flask import Blueprint

from .acl import acl_blueprint

platform_blueprint = Blueprint("platform", __name__)
