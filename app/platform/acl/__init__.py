from flask import Blueprint

from . import models, views#, api  # noqa

acl_blueprint = Blueprint("acl", __name__)
