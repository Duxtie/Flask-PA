# import datetime as date

from flask import Markup, url_for
# from flask_appbuilder import Model
from flask_appbuilder.filemanager import get_file_original_name
from flask_appbuilder.models.mixins import FileColumn
from sqlalchemy import Column, Date, ForeignKey, Integer, Float, String, Text
from sqlalchemy.orm import relationship
from sqlalchemy.schema import FetchedValue
from sqlalchemy.dialects.mssql import UNIQUEIDENTIFIER

from etas.app.hr.client.models import Client
from etas.app.hr.salary_plan.models import SalaryStructure, SalaryGrade, SalaryStep
from etas.app.models import BaseModel as Model
from etas.app.settings.state.models import State

import datetime

import uuid


class PayrollFileType(Model):
    __tablename__ = 'payroll_file_types'

    id = Column(Integer, primary_key=True)
    name = Column(String(191), unique=True, nullable=False)
    description = Column(Text(2000))

    def __repr__(self):
        return self.name


class PayrollFile(Model):
    __tablename__ = 'payroll_files'

    id = Column(Integer, primary_key=True)
    name = Column(String(191), unique=True, nullable=False)
    payment_date = Column(Date, nullable=False)

    client_id = Column(Integer, ForeignKey("clients.id"), default=0)
    client = relationship(Client)

    state_id = Column(Integer, ForeignKey("states.id"), default=0)
    state = relationship(State)

    type_id = Column(Integer, ForeignKey("payroll_file_types.id"), default=0)
    type = relationship(PayrollFileType)

    file = Column(FileColumn, nullable=False)
    description = Column(Text(2000))

    def __repr__(self):
        return self.name

    def download(self):
        return Markup(
            '<a href="'
            + url_for("PayrollFileModelView.download", filename=str(self.file))
            + '">Download</a>'
        )

    def file_name(self):
        return get_file_original_name(str(self.file))

    def month_year(self):
        return datetime.datetime(self.stat_date.year, self.stat_date.month, 1)


class Payroll(Model):
    __tablename__ = 'payrolls'

    id = Column(Integer, primary_key=True)

    client_id = Column(Integer, ForeignKey("clients.id"), default=0)
    client = relationship(Client)

    payment_date = Column(Date, nullable=False)
    ippis_id = Column(String(100), server_default=FetchedValue())
    # employee_id = Column(Integer, server_default=FetchedValue())
    # service_id = Column(Integer, server_default=FetchedValue())
    # designation_id = Column(Integer, server_default=FetchedValue())
    # department_id = Column(Integer, server_default=FetchedValue())
    # salary_structure_id = Column(ForeignKey('salary_structures.id'), server_default=FetchedValue())
    # salary_grade_id = Column(ForeignKey('salary_grades.id'), index=True, server_default=FetchedValue())
    # salary_step_id = Column(ForeignKey('salary_steps.id'), index=True, server_default=FetchedValue())
    # bank_id = Column(Integer, server_default=FetchedValue())
    # pension_provider_id = Column(Integer, server_default=FetchedValue())
    basic_pay = Column(Float(16, True), nullable=False)
    gross_pay = Column(Float(16, True), nullable=False)
    net_pay = Column(Float(16, True), nullable=False)
    employee_pension = Column(Float(16, True), nullable=False)
    employer_pension = Column(Float(16, True), nullable=False)
    cra = Column(Float(16, True), nullable=False)
    nhf = Column(Float(16, True), nullable=False)
    nhis = Column(Float(16, True), nullable=False)
    paye = Column(Float(16, True), nullable=False)
    loan_count = Column(Integer, nullable=False, default=0)
    total_loan_repayment = Column(Float(16, True), nullable=False)
    total_allowance = Column(Float(16, True), nullable=False)
    total_deduction = Column(Float(16, True), nullable=False)
    loan_total = Column(Float(10, True), index=True, server_default=FetchedValue())
    loans = Column(String(1000))
    salary_components = Column(String(1000))
    remarks = Column(String(191))
    # user_id = Column(Integer, server_default=FetchedValue())
    description = Column(String(700))

    # created_at = Column(DateTime, default=datetime.utcnow())
    # updated_at = Column(DateTime, default=datetime.utcnow())
    # deleted_at = Column(DateTime, nullable=True, default=False)

    # salary_structure = relationship(SalaryStructure,
    #                                 primaryjoin='Payroll.salary_structure_id == SalaryStructure.id',
    #                                 # backref='payrolls'
    #                                 )
    # salary_grade = relationship(SalaryGrade,
    #                             primaryjoin='Payroll.salary_grade_id == SalaryGrade.id',
    #                             # backref='payrolls'
    #                             )
    # salary_step = relationship(SalaryStep,
    #                            primaryjoin='Payroll.salary_step_id == SalaryStep.id',
    #                            # backref='payrolls'
    #                            )

    def __repr__(self):
        return self.ippis_id
