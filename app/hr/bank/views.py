# import calendar

# from flask_appbuilder import ModelView
# from flask_appbuilder.charts.views import GroupByChartView
# from flask_appbuilder.models.group import aggregate_count
from flask_appbuilder.models.sqla.interface import SQLAInterface

from etas.app.views import BaseModelView as ModelView
from .models import Bank, BankType
from ..views import route_prefix
from ... import appbuilder, db


class BankTypeModelView(ModelView):
    route_base = "/" + route_prefix + "/bank-type"
    datamodel = SQLAInterface(BankType)

    list_columns = ['name', 'updated_by', 'updated_at']

    add_exclude_columns = ModelView.add_exclude_columns
    edit_exclude_columns = add_exclude_columns


class BankModelView(ModelView):
    route_base = "/" + route_prefix + "/bank"
    datamodel = SQLAInterface(Bank)

    list_columns = ['name', 'bank_group', 'updated_by', 'updated_at']

    add_exclude_columns = ModelView.add_exclude_columns
    edit_exclude_columns = add_exclude_columns


# db.create_all()
appbuilder.add_view(
    BankModelView,
    "Bank",
    category="Bank",
    category_icon="fa-folder",
)

appbuilder.add_view(
    BankGroupModelView,
    "Bank Group",
    category="Bank",
    category_icon="fa-folder",
)
