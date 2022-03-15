from flask_appbuilder.models.sqla.interface import SQLAInterface

from etas.app.views import BaseModelView as ModelView
from .models import Employees
from ..views import route_prefix
from ... import appbuilder, db


class EmployeesModelView(ModelView):
    route_base = "/" + route_prefix + "/employee"
    datamodel = SQLAInterface(Employees)


appbuilder.add_view(
    EmployeesModelView,
    "Employees",
    category="BioData",
    category_icon="fa-folder",
)
