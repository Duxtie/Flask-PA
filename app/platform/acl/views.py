from flask import request, redirect, flash, g
from flask_appbuilder._compat import as_unicode
from flask_appbuilder.baseviews import expose
from flask_appbuilder.security.forms import LoginForm_db, ResetPasswordForm
from flask_appbuilder.security.registerviews import RegisterUserDBView
from flask_appbuilder.security.views import AuthView
from flask_appbuilder.security.views import UserDBModelView
from flask_appbuilder.security.views import UserInfoEditView
from flask_appbuilder.views import SimpleFormView
from flask_babel import lazy_gettext
from flask_login.utils import login_user

from .forms import UserInfoEdit
from .widgets import ACLUserListWidget
from ....config import APP_TEMPLATE


def get_template():
    template = ''
    try:
        # template = current_app.config['APP_TEMPLATE']
        template = APP_TEMPLATE
    except Exception as e:
        'philbert'
    return template


class ACLUserDBModelView(UserDBModelView):
    """
        View that add DB specifics to User view.
        Override to implement your own custom view.
        Then override userdbmodelview property on SecurityManager
    """

    add_template = get_template() + "/general/model/add.html"
    list_template = get_template() + "/general/model/list.html"
    show_template = get_template() + "/general/model/show.html"
    edit_template = get_template() + "/general/model/edit.html"

    list_widget = ACLUserListWidget

    show_fieldsets = [
        (
            lazy_gettext("User info"),
            {"fields": [
                "username",
                "active",
                "roles",
                "login_count",
                # "emp_number"
            ]},
        ),
        (
            lazy_gettext("Personal Info"),
            {"fields": ["first_name", "last_name", "middle_name", "email", "phone"], "expanded": True},
        ),
        (
            lazy_gettext("Audit Info"),
            {
                "fields": [
                    "last_login",
                    "fail_login_count",
                    "created_on",
                    "created_by",
                    "changed_on",
                    "changed_by",
                ],
                "expanded": False,
            },
        ),
    ]

    user_show_fieldsets = [
        (
            lazy_gettext("User info"),
            {"fields": [
                "username", "active", "roles", "login_count",
                # "emp_number"
            ]},
        ),
        (
            lazy_gettext("Personal Info"),
            {
                "fields": [
                    "first_name",
                    "last_name",
                    "email",
                    "phone"
                ], "expanded": True},
        ),
    ]

    add_columns = [
        "first_name",
        "last_name",
        "middle_name",
        "username",
        "active",
        "email",
        "phone",
        "roles",
        # "company",
        # "emp_number",
        "password",
        "conf_password",
    ]

    list_columns = [
        "first_name",
        "last_name",
        "middle_name",
        "username",
        "email",
        "phone",
        "active",
        "roles",
        # "company",
    ]

    edit_columns = [
        "first_name",
        "last_name",
        "middle_name",
        "username",
        "active",
        "email",
        "phone",
        "roles",
        # "company",
        # "emp_number",
    ]


class ACLUserInfoEditView(UserInfoEditView):
    form = UserInfoEdit


class ACLRegisterUserDBView(RegisterUserDBView):
    route_base = '/register'
    email_template = get_template() + '/general/security/register_mail.html'
    email_subject = lazy_gettext('Your Account activation')
    activation_template = get_template() + '/general/security/activation.html'
    form_title = lazy_gettext('Fill out the registration form')
    error_message = lazy_gettext('Not possible to register you at the moment, try again later')
    message = lazy_gettext('Registration sent to your email')


class ACLAuthDBView(AuthView):
    login_template = get_template() + "/general/security/login_db.html"

    @expose("/login/", methods=["GET", "POST"])
    def login(self):
        if g.user is not None and g.user.is_authenticated:
            return redirect(self.appbuilder.get_url_for_index)
        form = LoginForm_db()
        if form.validate_on_submit():
            user = self.appbuilder.sm.auth_user_db(
                form.username.data, form.password.data
            )
            if not user:
                flash(as_unicode(self.invalid_login_message), "warning")
                return redirect(self.appbuilder.get_url_for_login)
            login_user(user, remember=False)
            return redirect(self.appbuilder.get_url_for_index)
        return self.render_template(
            self.login_template, title=self.title, form=form, appbuilder=self.appbuilder
        )


class ResetPasswordView(SimpleFormView):
    """
        View for reseting all users password
    """

    route_base = "/reset-password"
    form = ResetPasswordForm
    form_title = lazy_gettext("Reset Password Form")
    redirect_url = "/"
    message = lazy_gettext("Password Changed")

    def form_post(self, form):
        pk = request.args.get("pk")
        self.appbuilder.sm.reset_password(pk, form.password.data)
        flash(as_unicode(self.message), "info")
