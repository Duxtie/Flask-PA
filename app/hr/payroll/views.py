# import calendar

import datetime

import pandas as pd
from flask import flash, redirect, request, Response, json
from flask.globals import _request_ctx_stack
from flask_appbuilder.actions import action
from flask_appbuilder.fields import AJAXSelectField
from flask_appbuilder.fieldwidgets import Select2AJAXWidget, Select2SlaveAJAXWidget
# from flask_appbuilder import ModelView
# from flask_appbuilder.charts.views import GroupByChartView
# from flask_appbuilder.models.group import aggregate_count
from flask_appbuilder.models.sqla.interface import SQLAInterface
from flask_babel import lazy_gettext as _
from wtforms import validators

from etas.app.views import BaseModelView as ModelView, BaseSimpleFormView as SimpleFormView
from etas.app.action import bulk_action
from .forms import PayrollImportForm
from .models import Payroll, PayrollFile, PayrollFileType
from ..views import route_prefix
from etas.app import appbuilder, db, get_template
from flask_appbuilder import expose, BaseView, IndexView, has_access
from dumper import dump
from sqlalchemy import Table, MetaData, select, alias
from sqlalchemy.sql import extract
from .compare.CompareString import PayrollCompare

try:
    from flask import _app_ctx_stack
except ImportError:
    _app_ctx_stack = None

app_stack = _app_ctx_stack or _request_ctx_stack


def dict_append(dict, key, value):
    if key not in dict:
        dict[key] = []
    dict[key].append(value)


class PayrollFileTypeModelView(ModelView):
    route_base = "/" + route_prefix + "/payroll-file-types"
    datamodel = SQLAInterface(PayrollFileType)

    list_columns = ['name', 'updated_by', 'updated_at']
    add_exclude_columns = ModelView.add_exclude_columns + ['is_active']
    edit_exclude_columns = add_exclude_columns


class PayrollFileModelView(ModelView):
    route_base = "/" + route_prefix + "/payroll-files"
    datamodel = SQLAInterface(PayrollFile)

    related_views = [PayrollFileType]

    # flash('Hello world!', "info")

    # extra_args = {'bulk_actions': {
    #     'populate_db': {
    #         'name': 'Populate Database',
    #     }
    # }}

    list_columns = ['name', 'client', 'payment_date', 'updated_by', 'updated_at']
    add_exclude_columns = ModelView.add_exclude_columns + ['is_active']
    edit_exclude_columns = add_exclude_columns

    # @bulk_action(
    #     "compare_data", "Compare Payroll", False, "fa-exchange"
    # )
    # def compare_data(self, item):
    #     """
    #         do something with the item record
    #     """
    #     # return render_template('')

    @action(
        "populate_db", "Populate Database", "You are about to import payroll to database, please confirm action",
        "fa-database"
    )
    def populate_db(self, items):
        ctx = app_stack.top
        base_path = ctx.app.config["UPLOAD_FOLDER"]

        # return request.form
        for item in items:
            path = item.file

            try:
                df = pd.read_excel(base_path + path)
            except Exception:
                df = pd.read_csv(base_path + path)

            for index, row in df.iterrows():

                payroll = Payroll()

                payroll.payment_date = item.payment_date
                payroll.ippis_id = row['STAFF ID']
                payroll.name = row['EMPLOYEE NAME']
                payroll.basic_pay = row['BASIC SALARY']

                try:
                    total_allowance = row['TOTAL ALLOWANCE']
                except:
                    total_allowance = 0

                payroll.total_allowance = total_allowance
                payroll.gross_pay = row['TOTAL GROSS']

                payroll.gross_pay = row['TOTAL GROSS']

                payroll.nhf = row['NHF']
                payroll.employee_pension = row['PENSION']
                payroll.employer_pension = row['PENSION']
                payroll.cra = 0
                payroll.nhis = 0
                payroll.paye = row['P.A.Y.E']

                payroll.total_loan_repayment = 0

                payroll.total_deduction = row['TOTAL DEDUCTION']
                payroll.net_pay = row['TOTAL NETPAY']

                db.session.add(payroll)
                db.session.commit()

        return redirect(self.get_redirect())


class PayrollModelView(ModelView):
    route_base = "/" + route_prefix + "/payroll"
    datamodel = SQLAInterface(Payroll)

    list_columns = ['payment_date', 'ippis_id', 'basic_pay', 'total_allowance', 'gross_pay', 'paye', 'total_deduction',
                    'net_pay']
    add_exclude_columns = ModelView.add_exclude_columns + ['is_active']
    edit_exclude_columns = add_exclude_columns

    add_form_extra_fields = {
        "salary_structure": AJAXSelectField(
            "Salary Structure",
            description="Salary structure is populated with AJAJ",
            datamodel=datamodel,
            validators=[validators.DataRequired()],
            col_name="salary_structure",
            widget=Select2AJAXWidget(
                endpoint="/" + route_prefix + "/salary_step/api/column/add/salary_structure"
            ),
        ),
        "salary_grade": AJAXSelectField(
            "Salary Grade",
            description="Salary grade is related to salary structure",
            datamodel=datamodel,
            validators=[validators.DataRequired()],
            col_name="salary_grade",
            widget=Select2SlaveAJAXWidget(
                master_id="salary_structure",
                endpoint="/" + route_prefix + "/salary_step/api/column/add/salary_grade?_flt_0_salary_structure_id={{ID}}",
            ),
        ),
        "salary_step": AJAXSelectField(
            "Salary Step",
            description="Salary step is related to Salary grade",
            datamodel=datamodel,
            validators=[validators.DataRequired()],
            col_name="salary_step",
            widget=Select2SlaveAJAXWidget(
                master_id="salary_grade",
                endpoint="/" + route_prefix + "/salary_step/api/column/add/salary_step?_flt_0_salary_grade_id={{ID}}",
                extra_classes='form-control'
            ),
        ),
    }

    edit_form_extra_fields = add_form_extra_fields


class PayrollCompareFormView(SimpleFormView):
    route_base = "/" + route_prefix + "/payroll-compare"
    form = PayrollImportForm
    form_title = _("Compare Payroll")
    message = "Compare request queued, file will be available shortly!"

    def form_get(self, form):
        form.field1.data = "This was prefilled"

    def form_post(self, form):
        # post process form
        flash(self.message, "info")


class PayrollCompareIndexView(BaseView):
    """
        A simple view that implements the index for the site
    """

    route_base = "/" + route_prefix + "/payroll-compare"
    default_view = "index"
    index_template = get_template() + '/pages/payroll/compare/index.html'

    @expose("/list", methods=['GET', 'POST'])
    @has_access
    def index(self):
        self.update_redirect()
        if request.method == 'POST':

            columns = request.form.getlist('columns[]')

            # metadata = MetaData()
            # payroll_query = db.session.query(Payroll.id)

            # payroll_1 = aliased(Payroll)
            # payroll_2 = aliased(Payroll)
            # session.query(User) \
            #     .join(Visit1, (Visit1.user_id == User.id) & (Visit1.visit_number == 1)) \
            #     .join(Visit2, (Visit2.user_id == User.id) & (Visit2.visit_number == 2)) \
            #     .values(User.id, Visit1.Score - Visit2.Score)

            # payroll = Table('payrolls', metadata,)

            # columns = []
            # for column in request.form.getlist('columns[]'):
            #     columns += column
            # return payroll_query
            # return str(request.form)
        # return Response('Index Page')
        print(request.form)
        return self.render_template(self.index_template, appbuilder=self.appbuilder)


class PayrollCompareModalView(BaseView):
    route_base = "/" + route_prefix + "/payroll-compare"
    default_view = "index"
    index_template = get_template() + '/pages/payroll/compare/index.html'
    modal_template = get_template() + '/pages/payroll/compare/modal-form.html'
    form_template = get_template() + '/pages/payroll/compare/form.html'

    @expose("/list", methods=['GET', 'POST'])
    @has_access
    def index(self):
        self.update_redirect()
        if request.method == 'POST':

            columns = request.form.getlist('columns[]')

            # metadata = MetaData()
            # payroll_query = db.session.query(Payroll.id)

            # payroll_1 = aliased(Payroll)
            # payroll_2 = aliased(Payroll)
            # session.query(User) \
            #     .join(Visit1, (Visit1.user_id == User.id) & (Visit1.visit_number == 1)) \
            #     .join(Visit2, (Visit2.user_id == User.id) & (Visit2.visit_number == 2)) \
            #     .values(User.id, Visit1.Score - Visit2.Score)

            # payroll = Table('payrolls', metadata,)

            # columns = []
            # for column in request.form.getlist('columns[]'):
            #     columns += column
            # return payroll_query
            # return str(request.form)
        # return Response('Index Page')
        print(request.form)
        return self.render_template(self.index_template, appbuilder=self.appbuilder)

    @expose("/modal")
    @has_access
    def create(self):
        self.update_redirect()

        self.index_template = self.form_template
        if request.args.get('view') == 'modal':
            self.index_template = self.modal_template

        if request.method == 'POST':
            return json.dumps(request.form)
        else:
            table_name = Payroll.__table__.name
            table_columns = Payroll.__table__.columns
            table_included_columns = ['basic_pay', 'gross_pay', 'pension', 'cra', 'nhis', 'nhs', 'pension', 'total_allowance', 'total_deduction']
            table_included_columns = []

            def make_db_column(columns, tbl_included_columns):
                new_columns = {}
                for table_column in columns:
                    table_column = str(table_column).replace(str(table_name+'.'), '')

                    if table_column in tbl_included_columns:
                        table_column_label = table_column.replace('_', ' ')
                        dict_append(new_columns, table_column, table_column_label)

                return new_columns

            tbl_columns = make_db_column(table_columns, table_included_columns)
            profile_columns = ['EMPLOYEE NAME', 'JOB TITLE', 'BANK NAME', 'ACCOUNT NUMBER', 'GRADE', 'STEP', 'LOCATION',
                               'DEPARTMENT', 'PFA NAME', 'PIN NO']
            payroll_columns = ['BASIC SALARY', 'TOTAL ALLOWANCE', 'TOTAL GROSS', 'PENSION', 'P.A.Y.E', 'TOTAL DEDUCTION',
                               'TOTAL NETPAY']

            return self.render_template(self.index_template,
                                        appbuilder=self.appbuilder,
                                        tbl_columns=tbl_columns,
                                        profile_columns=profile_columns,
                                        payroll_columns=payroll_columns
                                        )

    @expose("/store", methods=['POST'])
    @has_access
    def store(self):
        self.update_redirect()

        if request.method == 'POST':
            def get_month(date):
                return datetime.datetime.strptime(date, '%Y-%m').strftime("%m")

            def get_year(date):
                return datetime.datetime.strptime(date, '%Y-%m').strftime("%Y")

            def get_payroll_file(date):
                return db.session.query(PayrollFile).filter(
                    extract('year', PayrollFile.payment_date) == get_year(date),
                    extract('month', PayrollFile.payment_date) == get_month(date)).first()

            first_date = request.form.get('month_1')
            second_date = request.form.get('month_2')

            columns = []
            for column in request.form.getlist('columns[]'):
                columns += [column.replace('_', ' ').upper()]

            first_file = get_payroll_file(first_date)
            second_file = get_payroll_file(second_date)

            # profile_columns = ['Staff ID', 'Full Name', 'Job Title', 'Institution', 'Bank Name', 'Account Number',
            #                    'Grade', 'Grade Step']
            # payroll_columns = ['Staff ID', 'Total Gross', 'Total Deduction', 'Net Pay']
            # columns = profile_columns + payroll_columns



            PayrollCompare(old_file=first_file.file, new_file=second_file.file, columns=columns, key='STAFF ID').compare()


            return json.dumps(first_file.file)

            records = db.session.query(PayrollFile).order_by(PayrollFile.id).all()
            for record in records:
                return json.dumps(record.name)

            # file_model = SQLAInterface(PayrollFile)

            # file_model = file_model.query()

            # old = PayrollFile.query.get()
            old = db.session.query(PayrollFile)
            # old = PayrollFile.filter(PayrollFile.payment_date, str('old_date'))

            # return json.dumps(records)
            return json.dumps(request.form)

        return self.render_template(self.index_template, appbuilder=self.appbuilder, tbl_columns=tbl_columns)

    @expose('/test', methods=['GET'])
    def test(self):
        test_template = get_template() + '/pages/payroll/compare/test.html'
        var = {'compare_label': 'Compare Files'}
        extra_args = {
            'buttons':
                {
                    'compare': {
                        'label': var['compare_label'],
                        'attrs': {
                            'data-title': var['compare_label'],
                            'data-href': '#',
                            'data-act': 'ajax-modal',
                            'data-modal-size': 'modal-lg',
                        }
                    }
                }
            ,
            "extra_arg_obj1": "Extra argument 1 injected"
        }
        return self.render_template(test_template, extra_args=extra_args)


# db.create_all()
appbuilder.add_view(
    PayrollModelView,
    "Payroll",
    category="Payroll Manager",
    category_icon="fa-folder",
)

appbuilder.add_view(
    PayrollFileModelView,
    "Payroll FIle",
    label=_("Payroll FIle"),
    category="Payroll Manager",
    category_icon="fa-folder",
)

appbuilder.add_view(
    PayrollFileTypeModelView,
    "Payroll FIle Type",
    label=_("Payroll FIle Type"),
    category="Payroll Manager",
    category_icon="fa-folder",
)

appbuilder.add_view(
    PayrollCompareFormView,
    "My form View",
    label=_("Compare Payroll"),
    category="Payroll Manager",
    category_icon="fa-folder",
)


appbuilder.add_view_no_menu(PayrollCompareIndexView())
appbuilder.add_view_no_menu(PayrollCompareModalView())
