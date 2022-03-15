from flask_appbuilder.api import ModelRestApi
from flask_appbuilder.models.sqla.interface import SQLAInterface

from .models import ACLUser


# from ... import appbuilder


class ACLUserModelApi(ModelRestApi):
    resource_name = 'users'
    datamodel = SQLAInterface(ACLUser)
    allow_browser_login = True

    list_title = 'Users'

    list_columns = [
        'id', 'first_name', 'last_name', 'middle_name', 'date_of_birth',
        'email', 'phone', 'avatar', 'is_active', 'created_at', 'updated_at', 'roles', 'status',
        'last_ip'
    ]

# appbuilder.add_api(ACLUserModelApi)
