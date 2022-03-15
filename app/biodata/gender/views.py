from flask_appbuilder.models.sqla.interface import SQLAInterface

from etas.app.views import BaseModelView as ModelView
from .models import Gender
from ..views import route_prefix
from ... import appbuilder, db


def fill_gender():
    try:
        db.session.add(Gender(id=1, name="Male"))
        db.session.add(Gender(id=2, name="Female"))
        db.session.add(Gender(id=9, name="Non-binary"))
        db.session.commit()
    except Exception:
        db.session.rollback()


class GenderModelView(ModelView):
    route_base = "/" + route_prefix + "/gender"
    datamodel = SQLAInterface(Gender)


# db.create_all()
fill_gender()

appbuilder.add_view(
    GenderModelView,
    "Gender",
    category="BioData",
    category_icon="fa-folder",
)
