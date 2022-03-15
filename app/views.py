import logging

from flask import render_template, redirect
# from flask_appbuilder.models.sqla.interface import SQLAInterface
# from flask_appbuilder import ModelView, ModelRestApi
from flask_appbuilder import ModelView, SimpleFormView
from flask_appbuilder.actions import action
# from flask_appbuilder.actions import action
from flask_appbuilder.const import PERMISSION_PREFIX

from etas.app import appbuilder, get_template
from etas.app.action import BaseActionItem
# from flask_appbuilder.fieldwidgets import Select2Widget
# from wtforms.fields import DateField
# from .fieldwidgets import BS3TFROWidget
from etas.app.widgets import FormWidget, ListWidget, ShowWidget

# from fab_addon_audit.views import AuditedModelView

# define default excluded columns

log = logging.getLogger(__name__)


class BaseModelView(ModelView):
    add_template = get_template() + '/general/model/add.html'
    """ Your own add jinja2 template for add """
    list_template = get_template() + '/general/model/list.html'
    """ Your own add jinja2 template for list """
    show_template = get_template() + '/general/model/show.html'
    """ Your own add jinja2 template for show """
    edit_template = get_template() + '/general/model/edit_cascade.html'
    """ Your own add jinja2 template for edit """

    list_widget = ListWidget
    """ List widget override """
    edit_widget = FormWidget
    """ Edit widget override """
    add_widget = FormWidget
    """ Add widget override """
    show_widget = ShowWidget
    """ Show widget override """

    exclude_columns = ["created_by", "updated_by", "created_at", "updated_at", "deleted_at"]
    add_exclude_columns = exclude_columns
    edit_exclude_columns = add_exclude_columns

    add_form_extra_fields = {
        # 'created_at': DateField('created_at', widget=BS3TFROWidget)
    }

    edit_form_extra_fields = add_form_extra_fields

    bulk_actions = None

    def __init__(self, **kwargs):
        super(BaseModelView, self).__init__(**kwargs)
        # collect and setup bulk_actions
        self.bulk_actions = {}
        for attr_name in dir(self):
            func = getattr(self, attr_name)
            if hasattr(func, "_bulk_action"):
                bulk_action = BaseActionItem(*func._bulk_action, func=func)
                permission_name = bulk_action.name
                # Infer previous if not declared
                if self.method_permission_name.get(attr_name):
                    if not self.previous_method_permission_name.get(attr_name):
                        self.previous_method_permission_name[attr_name] = bulk_action.name
                    permission_name = (
                            PERMISSION_PREFIX + self.method_permission_name.get(attr_name)
                    )
                if permission_name not in self.base_permissions:
                    self.base_permissions.append(permission_name)
                self.bulk_actions[bulk_action.name] = bulk_action

    # @bulk_action("muldelete", "Delete", "Delete all Really?", "fa-rocket")
    # def muldelete(self, items):
    #     if isinstance(items, list):
    #         self.datamodel.delete_all(items)
    #         self.update_redirect()
    #     else:
    #         self.datamodel.delete(items)
    #     return redirect(self.get_redirect())

    @action("muldelete", "Delete", "Delete all Really?", "fa-trash")
    def muldelete(self, items):
        if isinstance(items, list):
            self.datamodel.delete_all(items)
            self.update_redirect()
        else:
            self.datamodel.delete(items)
        return redirect(self.get_redirect())

    def _get_list_widget(
            self,
            filters,
            actions=None,
            bulk_actions=None,
            order_column="",
            order_direction="",
            page=None,
            page_size=None,
            widgets=None,
            **args,
    ):

        """ get joined base filter and current active filter for query """
        widgets = widgets or {}
        actions = actions or self.actions
        bulk_actions = bulk_actions or self.bulk_actions
        page_size = page_size or self.page_size
        if not order_column and self.base_order:
            order_column, order_direction = self.base_order
        joined_filters = filters.get_joined_filters(self._base_filters)
        count, lst = self.datamodel.query(
            joined_filters,
            order_column,
            order_direction,
            page=page,
            page_size=page_size,
        )
        pks = self.datamodel.get_keys(lst)

        # serialize composite pks
        pks = [self._serialize_pk_if_composite(pk) for pk in pks]

        widgets["list"] = self.list_widget(
            label_columns=self.label_columns,
            include_columns=self.list_columns,
            value_columns=self.datamodel.get_values(lst, self.list_columns),
            order_columns=self.order_columns,
            formatters_columns=self.formatters_columns,
            page=page,
            page_size=page_size,
            count=count,
            pks=pks,
            actions=actions,
            bulk_actions=bulk_actions,
            filters=filters,
            modelview_name=self.__class__.__name__,
        )
        return widgets


"""
    Create your Model based REST API::

    class MyModelApi(ModelRestApi):
        datamodel = SQLAInterface(MyModel)

    appbuilder.add_api(MyModelApi)


    Create your Views::


    class MyModelView(ModelView):
        datamodel = SQLAInterface(MyModel)


    Next, register your Views::


    appbuilder.add_view(
        MyModelView,
        "My View",
        icon="fa-folder-open-o",
        category="My Category",
        category_icon='fa-envelope'
    )
"""

"""
    Application wide 404 error handler
"""


class BaseSimpleFormView(SimpleFormView):
    """
        View for presenting your own forms
        Inherit from this view to provide some base processing
        for your customized form views.

        Notice that this class inherits from BaseView so all properties
        from the parent class can be overridden also.

        Implement form_get and form_post to implement your
        form pre-processing and post-processing
    """

    form_template = get_template() + '/general/model/edit.html'

    edit_widget = FormWidget


@appbuilder.app.errorhandler(404)
def page_not_found(e):
    return (
        render_template(get_template() + "/errors/404.html",
                        base_template=appbuilder.base_template,
                        appbuilder=appbuilder
                        ), 404,
    )

# class BaseAuditedModelView(AuditedModelView):
#     pass
