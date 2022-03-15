from flask_appbuilder.models.sqla.interface import SQLAInterface

from etas.app.views import BaseModelView as ModelView
from .models import Title
from ..views import route_prefix
from ... import appbuilder, db


def fill_title():
    items = [
        {'id': 1, 'name': 'Mr.'},
        {'id': 2, 'name': 'Mrs.'},
        {'id': 3, 'name': 'Dr.'},
        {'id': 1000, 'name': 'Unspecified'},
    ]
    try:
        index = 0
        while index < len(items):
            db.session.add(Title(id=items[index]['id'], name=items[index]['name']))
            index += 1
        db.session.commit()
    except Exception:
        db.session.rollback()


class TitleModelView(ModelView):
    route_base = "/" + route_prefix + "/title"
    datamodel = SQLAInterface(Title)


# db.create_all()
fill_title()

appbuilder.add_view(
    TitleModelView,
    "Title",
    category="BioData",
    category_icon="fa-folder",
)
