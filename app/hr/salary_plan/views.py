# import calendar

from flask_appbuilder.fields import AJAXSelectField
from flask_appbuilder.fieldwidgets import Select2AJAXWidget, Select2SlaveAJAXWidget
# from flask_appbuilder import ModelView
# from flask_appbuilder.charts.views import GroupByChartView
# from flask_appbuilder.models.group import aggregate_count
from flask_appbuilder.models.sqla.interface import SQLAInterface
from wtforms import validators

from etas.app.views import BaseModelView as ModelView
from .models import SalaryStructure, SalaryGrade, SalaryStep
from ..views import route_prefix
from ... import appbuilder, db


class SalaryStructureModelView(ModelView):
    route_base = "/" + route_prefix + "/salary_structure"
    datamodel = SQLAInterface(SalaryStructure)

    list_columns = ['name', 'description']
    add_columns = ['name', 'description']

    add_exclude_columns = ModelView.add_exclude_columns + ['is_active']
    edit_exclude_columns = add_exclude_columns


class SalaryGradeModelView(ModelView):
    route_base = "/" + route_prefix + "/salary_grade"
    datamodel = SQLAInterface(SalaryGrade)

    list_columns = ['name', 'salary_structure', 'updated_at']
    add_exclude_columns = ModelView.add_exclude_columns + ['is_active']


class SalaryStepModelView(ModelView):
    route_base = "/" + route_prefix + "/salary_step"
    datamodel = SQLAInterface(SalaryStep)

    list_columns = ['name', 'salary_structure', 'salary_grade', 'updated_at']
    add_exclude_columns = ModelView.add_exclude_columns + ['is_active']

    add_form_extra_fields = {
        "salary_structure": AJAXSelectField(
            "Salary Structure",
            description="Group field populated with AJAX",
            datamodel=datamodel,
            validators=[validators.DataRequired()],
            col_name="salary_structure",
            widget=Select2AJAXWidget(
                endpoint="/" + route_prefix + "/salary_step/api/column/add/salary_structure"
            ),
        ),
        "salary_grade": AJAXSelectField(
            "Salary Grade",
            description="Sub Group related to Group",
            datamodel=datamodel,
            validators=[validators.DataRequired()],
            col_name="salary_grade",
            widget=Select2SlaveAJAXWidget(
                master_id="salary_structure",
                endpoint="/" + route_prefix + "/salary_step/api/column/add/salary_grade?_flt_0_salary_structure_id={{ID}}",
            ),
        ),
    }

    edit_form_extra_fields = add_form_extra_fields


# db.create_all()
appbuilder.add_view(
    SalaryStepModelView,
    "Salary Step",
    category="Salary Plan",
    category_icon="fa-folder",
)
appbuilder.add_view(
    SalaryGradeModelView,
    "Salary Grade",
    category="Salary Plan",
    category_icon="fa-folder",
)
appbuilder.add_view(
    SalaryStructureModelView,
    "Salary Structure",
    category="Salary Plan",
    category_icon="fa-folder",
)
