from flask_appbuilder.models.sqla.interface import SQLAInterface

from etas.app.views import BaseModelView as ModelView
from .models import Occupation
from ..views import route_prefix
from ... import appbuilder, db


def fill_occupation():
    try:
        db.session.add(Occupation(id=1, name="Developer"))
        db.session.add(Occupation(id=2, name="Doctor"))
        db.session.add(Occupation(id=1000, name="Unspecified"))
        db.session.commit()
    except Exception:
        db.session.rollback()


class OccupationModelView(ModelView):
    route_base = "/" + route_prefix + "/occupation"
    datamodel = SQLAInterface(Occupation)


# db.create_all()
fill_occupation()

appbuilder.add_view(
    OccupationModelView,
    "Occupation",
    category="BioData",
    category_icon="fa-folder",
)
