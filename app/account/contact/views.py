import calendar
import logging
import uuid

# from flask import (request, flash, json)
# from flask_appbuilder.charts.views import GroupByChartView
# from flask_appbuilder.models.group import aggregate_count
from flask_appbuilder.models.sqla.interface import SQLAInterface
from flask_appbuilder.security.decorators import has_access
from flask_appbuilder.baseviews import expose

from etas.app.views import BaseModelView as ModelView
from .models import Contact, ContactStatus
from .widgets import ContactEditBlockWidget
from ... import appbuilder, db

log = logging.getLogger(__name__)


# from ..views import route_prefix


def fill_contact_status():
    items = [
        {'id': 1, 'name': 'Active'},
        {'id': 2, 'name': 'Inactive'},
        {'id': 3, 'name': 'Suspended'},
        {'id': 4, 'name': 'Deceased'},
        {'id': 1000, 'name': 'Unspecified'}
    ]
    try:
        index = 0
        while index < len(items):
            db.session.add(ContactStatus(id=items[index]['id'], name=items[index]['name']))
            index += 1
        db.session.commit()
    except Exception:
        db.session.rollback()


def contact_add_fieldset():
    return [
        (
            "Summary",
            {
                "fields": [
                    "first_name",
                    "last_name",
                    "middle_name",
                    "title",
                    "gender",
                ]
            }
        ),
        (
            "Personal Info",
            {
                "fields": [
                    "designation",
                ],
                "expanded": False,
            },
        ),

    ]


def contact_show_fieldset():
    return [
        (
            "Summary",
            {
                "fields": [
                    "first_name",
                    "last_name",
                    "middle_name",
                    "gender",
                ]
            }
        ),
    ]


class ContactModelView(ModelView):
    route_base = "/contact"
    datamodel = SQLAInterface(Contact)

    edit_widget = ContactEditBlockWidget

    list_columns = ["full_name", "gender.name", "contact_status.name"]

    base_order = ("created_at", "asc")
    add_fieldsets = contact_add_fieldset()

    # show_fieldsets = contact_show_fieldset()

    # edit_fieldsets = add_fieldsets

    def pre_add(self, item):
        """
            Override this, will be called before add.
            If an exception is raised by this method,
            the message is shown to the user and the add operation is aborted.
        """
        # item.facility_id = 1
        item.uuid = uuid.uuid4()
        # item.cause_of_death = 'Old age'
        # pass

    """
    --------------------------------
            SHOW
    --------------------------------
    """

    @expose("/show/<pk>", methods=["GET"])
    @has_access
    def show(self, pk):
        pk = self._deserialize_pk_if_composite(pk)
        widgets = self._show(pk)

        return self.render_template(
            self.show_template,
            pk=pk,
            title=self.show_title,
            widgets=widgets,
            related_views=self._related_views,
        )


# class GroupModelView(ModelView):
#     route_base = "/" + route_prefix + "/contact-group"
#     datamodel = SQLAInterface(ContactGroup)
#     related_views = [ContactModelView]


def pretty_month_year(value):
    return calendar.month_name[value.month] + " " + str(value.year)


def pretty_year(value):
    return str(value.year)


# class ContactTimeChartView(GroupByChartView):
#     datamodel = SQLAInterface(Contact)
#
#     chart_title = "Grouped Birth contacts"
#     chart_type = "AreaChart"
#     label_columns = ContactModelView.label_columns
#     definitions = [
#         {
#             "group": "month_year",
#             "formatter": pretty_month_year,
#             "series": [(aggregate_count, "group")],
#         },
#         {
#             "group": "year",
#             "formatter": pretty_year,
#             "series": [(aggregate_count, "group")],
#         },
#     ]

fill_contact_status()

# appbuilder.add_view(
#     GroupModelView,
#     "Groups",
#     icon="fa-folder-open-o",
#     category="Contacts",
#     category_icon="fa-envelope",
# )
appbuilder.add_view(
    ContactModelView,
    "Contacts",
    icon="fa-envelope",
    # category="Account"
)
# appbuilder.add_separator("Contacts")
# appbuilder.add_view(
#     ContactTimeChartView,
#     "Contacts Birth Chart",
#     icon="fa-dashboard",
#     category="Contacts",
# )
