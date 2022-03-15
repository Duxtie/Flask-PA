from flask_appbuilder.models.sqla.interface import SQLAInterface

from etas.app.views import BaseModelView as ModelView
from .models import MaritalStatus
from ..views import route_prefix
from ... import appbuilder, db


def fill_marital_status():
    items = [
        {'id': 1, 'name': 'Single'},
        {'id': 2, 'name': 'Married'},
        {'id': 3, 'name': 'Divorced'},
        {'id': 4, 'name': 'Widowed'},
        {'id': 1000, 'name': 'Unspecified'},
    ]
    try:
        index = 0
        while index < len(items):
            db.session.add(MaritalStatus(id=items[index]['id'], name=items[index]['name']))
            index += 1
        db.session.commit()
    except Exception:
        db.session.rollback()


class MaritalStatusModelView(ModelView):
    route_base = "/" + route_prefix + "/marital_status"
    datamodel = SQLAInterface(MaritalStatus)


fill_marital_status()

appbuilder.add_view(
    MaritalStatusModelView,
    "Marital Status",
    category="BioData",
    category_icon="fa-folder",
)
