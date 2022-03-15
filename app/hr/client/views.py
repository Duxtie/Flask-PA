# import calendar

# from flask_appbuilder import ModelView
# from flask_appbuilder.charts.views import GroupByChartView
# from flask_appbuilder.models.group import aggregate_count
from flask_appbuilder.models.sqla.interface import SQLAInterface

from etas.app.views import BaseModelView as ModelView
from .models import Client, ClientGroup, ClientType
from ..views import route_prefix
from ... import appbuilder, db


class ClientTypeModelView(ModelView):
    route_base = "/" + route_prefix + "/client-type"
    datamodel = SQLAInterface(ClientType)

    list_columns = ['name', 'updated_by', 'updated_at']

    add_exclude_columns = ModelView.add_exclude_columns
    edit_exclude_columns = add_exclude_columns


class ClientGroupModelView(ModelView):
    route_base = "/" + route_prefix + "/client-group"
    datamodel = SQLAInterface(ClientGroup)

    list_columns = ['name', 'updated_by', 'updated_at']

    add_exclude_columns = ModelView.add_exclude_columns
    edit_exclude_columns = add_exclude_columns


class ClientModelView(ModelView):
    route_base = "/" + route_prefix + "/client"
    datamodel = SQLAInterface(Client)

    list_columns = ['name', 'client_group', 'updated_by', 'updated_at']

    add_exclude_columns = ModelView.add_exclude_columns
    edit_exclude_columns = add_exclude_columns


# db.create_all()
appbuilder.add_view(
    ClientModelView,
    "Client",
    category="Client",
    category_icon="fa-folder",
)

appbuilder.add_view(
    ClientGroupModelView,
    "Client Group",
    category="Client",
    category_icon="fa-folder",
)
