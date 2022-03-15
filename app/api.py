from .platform.acl.api import ACLUserModelApi

from etas.app import appbuilder

appbuilder.add_api(ACLUserModelApi)
