from flask_appbuilder.models.sqla.interface import SQLAInterface

from etas.app.views import BaseModelView as ModelView
from .models import Religion
from ..views import route_prefix
from ... import appbuilder, db


def fill_religion():
    items = [
        {'id': 1, 'name': 'Christian'},
        {'id': 2, 'name': 'Muslims'},
        {'id': 3, 'name': 'Buddhist'},
        {'id': 4, 'name': 'Not religious'},
        {'id': 1000, 'name': 'Unspecified'}
    ]
    try:
        index = 0
        while index < len(items):
            db.session.add(Religion(id=items[index]['id'], name=items[index]['name']))
            index += 1
        db.session.commit()
    except Exception:
        db.session.rollback()


class ReligionModelView(ModelView):
    route_base = "/" + route_prefix + "/religion"
    datamodel = SQLAInterface(Religion)


# db.create_all()
fill_religion()

appbuilder.add_view(
    ReligionModelView,
    "Religion",
    category="BioData",
    category_icon="fa-folder",
)
