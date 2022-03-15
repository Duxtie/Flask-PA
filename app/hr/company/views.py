# import calendar

# from flask_appbuilder import ModelView
# from flask_appbuilder.charts.views import GroupByChartView
# from flask_appbuilder.models.group import aggregate_count
from flask_appbuilder.models.sqla.interface import SQLAInterface

from etas.app.views import BaseModelView as ModelView
from .models import Company, CompanyGroup
from ..views import route_prefix
from ... import appbuilder, db


class CompanyGroupModelView(ModelView):
    route_base = "/" + route_prefix + "/company-group"
    datamodel = SQLAInterface(CompanyGroup)

    add_exclude_columns = ModelView.add_exclude_columns
    edit_exclude_columns = add_exclude_columns


class CompanyModelView(ModelView):
    route_base = "/" + route_prefix + "/company"
    datamodel = SQLAInterface(Company)

    add_exclude_columns = ModelView.add_exclude_columns
    edit_exclude_columns = add_exclude_columns


# db.create_all()
appbuilder.add_view(
    CompanyModelView,
    "Company",
    category="Company",
    category_icon="fa-folder",
)

appbuilder.add_view(
    CompanyGroupModelView,
    "Company Group",
    category="Company",
    category_icon="fa-folder",
)
