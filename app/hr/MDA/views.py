# import calendar

# from flask_appbuilder import ModelView
# from flask_appbuilder.charts.views import GroupByChartView
# from flask_appbuilder.models.group import aggregate_count
from flask_appbuilder.models.sqla.interface import SQLAInterface

from etas.app.views import BaseModelView as ModelView
from .models import MDA, MDAGroup, MDAType
from ..views import route_prefix
from ... import appbuilder, db


class MDATypeModelView(ModelView):
    route_base = "/" + route_prefix + "/mda-type"
    datamodel = SQLAInterface(MDAType)

    list_columns = ['name', 'updated_by', 'updated_at']

    add_exclude_columns = ModelView.add_exclude_columns
    edit_exclude_columns = add_exclude_columns


class MDAGroupModelView(ModelView):
    route_base = "/" + route_prefix + "/mda-group"
    datamodel = SQLAInterface(MDAGroup)

    list_columns = ['name', 'updated_by', 'updated_at']

    add_exclude_columns = ModelView.add_exclude_columns
    edit_exclude_columns = add_exclude_columns


class MDAModelView(ModelView):
    route_base = "/" + route_prefix + "/mda"
    datamodel = SQLAInterface(MDA)

    list_columns = ['name', 'mda_group', 'updated_by', 'updated_at']

    add_exclude_columns = ModelView.add_exclude_columns
    edit_exclude_columns = add_exclude_columns


# db.create_all()
appbuilder.add_view(
    MDAModelView,
    "MDA",
    category="MDA",
    category_icon="fa-folder",
)

appbuilder.add_view(
    MDAGroupModelView,
    "MDA Group",
    category="MDA",
    category_icon="fa-folder",
)
