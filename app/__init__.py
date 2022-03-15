import logging
import os

from flask import Flask
from flask_appbuilder import AppBuilder, SQLA
from flask_debugtoolbar import DebugToolbarExtension
from flask_migrate import Migrate
from flask_mail import Mail, Message
from flask_uuid import FlaskUUID

from etas.app.index import MyIndexView
from etas import config

from .platform.support.security.sec import ACLSecurityManager

APP_DIR = os.path.dirname(__file__)
CONFIG_MODULE = os.environ.get("FRIPZ_CONFIG", "etas.config")

if not os.path.exists(config.DATA_DIR):
    os.makedirs(config.DATA_DIR)

"""
 Logging configuration
"""

logging.basicConfig(format="%(asctime)s:%(levelname)s:%(name)s:%(message)s")
logging.getLogger().setLevel(logging.DEBUG)


def get_template():
    return config.APP_TEMPLATE


app = Flask(__name__)
# app.config.from_object("config")
app.config.from_object(CONFIG_MODULE)
db = SQLA(app)

flask_uuid = FlaskUUID()
flask_uuid.init_app(app)

migrate = Migrate(app, db)
mail = Mail(app)

# the toolbar is only enabled in debug mode:
app.debug = False

toolbar = DebugToolbarExtension(app)

appbuilder = AppBuilder(app, db.session,
                        indexview=MyIndexView,
                        base_template=get_template() + '/baselayout.html',
                        security_manager_class=ACLSecurityManager,
                        # static_folder="static/slick"
                        # , static_url_path="/slick",
                        )

"""
from sqlalchemy.engine import Engine
from sqlalchemy import event

#Only include this for SQLLite constraints
@event.listens_for(Engine, "connect")
def set_sqlite_pragma(dbapi_connection, connection_record):
    # Will force sqllite contraint foreign keys
    cursor = dbapi_connection.cursor()
    cursor.execute("PRAGMA foreign_keys=ON")
    cursor.close()
"""

from etas.app import views
from .api import ACLUserModelApi

def register_blueprint(app):
    # Import blueprints
    from .platform import platform_blueprint
    from .account import account_blueprint
    from .biodata import biodata_blueprint
    from .hr import hr_blueprint
    # from .medical_history import medical_history_blueprint
    # from .operation import operation_blueprint
    # from .dashboard import dashboard_blueprint
    # from .settings import system_setting_blueprint

    # Register blue prints
    app.register_blueprint(platform_blueprint)
    app.register_blueprint(account_blueprint)
    app.register_blueprint(hr_blueprint)
    app.register_blueprint(biodata_blueprint)
    # app.register_blueprint(medical_history_blueprint)
    # app.register_blueprint(operation_blueprint)
    # app.register_blueprint(dashboard_blueprint)
    # app.register_blueprint(system_setting_blueprint)


register_blueprint(app)

db.create_all()
