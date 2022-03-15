from flask_appbuilder.security.sqla.manager import SecurityManager

from ....platform.acl.models import ACLUser
from ....platform.acl.views import ACLRegisterUserDBView, ACLUserInfoEditView, ACLAuthDBView, ResetPasswordView
from ...acl.views import ACLUserDBModelView


class ACLSecurityManager(SecurityManager):
    user_model = ACLUser

    userdbmodelview = ACLUserDBModelView
    userinfoeditview = ACLUserInfoEditView

    registeruserdbview = ACLRegisterUserDBView

    authdbview = ACLAuthDBView

    resetpasswordview = ResetPasswordView
