from flask_appbuilder.models.sqla.interface import SQLAInterface

from etas.app.views import BaseModelView as ModelView
from .models import Designations
from ..views import route_prefix
from ... import appbuilder, db


def fill_occupation():
    try:
        db.session.add(Designations(id=1, name="Developer"))
        db.session.add(Designations(id=2, name="Doctor"))
        db.session.add(Designations(id=1000, name="Unspecified"))
        db.session.commit()
    except Exception:
        db.session.rollback()


class DesignationsModelView(ModelView):
    route_base = "/" + route_prefix + "/designation"
    datamodel = SQLAInterface(Designations)


# db.create_all()
fill_occupation()

appbuilder.add_view(
    DesignationsModelView,
    "Designations",
    category="BioData",
    category_icon="fa-folder",
)
