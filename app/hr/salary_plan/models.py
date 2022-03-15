# import datetime as date
from datetime import datetime

from flask_appbuilder import Model
from sqlalchemy import Column, DateTime, ForeignKey, Integer, Float, String
from sqlalchemy.orm import relationship
from sqlalchemy.schema import FetchedValue
from etas.app.models import BaseModel as Model


# from ..payroll.models import Payroll

# mindate = datetime.date(date.MINYEAR, 1, 1)


class SalaryStructure(Model):
    __tablename__ = 'salary_structures'

    id = Column(Integer, primary_key=True)
    name = Column(String(191), unique=True, nullable=False)
    description = Column(String(700))
    created_at = Column(DateTime, default=datetime.utcnow())
    updated_at = Column(DateTime, default=datetime.utcnow())
    deleted_at = Column(DateTime, nullable=True, default=False)

    def __repr__(self):
        return self.name


class SalaryGrade(Model):
    __tablename__ = 'salary_grades'

    id = Column(Integer, primary_key=True)
    name = Column(String(191), unique=True, nullable=False)
    salary_structure_id = Column(ForeignKey('salary_structures.id'), index=True, server_default=FetchedValue())
    description = Column(String(700))
    created_at = Column(DateTime, default=datetime.utcnow())
    updated_at = Column(DateTime, default=datetime.utcnow())
    deleted_at = Column(DateTime, nullable=True, default=False)

    salary_structure = relationship('SalaryStructure',
                                    primaryjoin='SalaryGrade.salary_structure_id == SalaryStructure.id',
                                    # backref='salary_grades'
                                    )

    def __repr__(self):
        return self.name


class SalaryStep(Model):
    __tablename__ = 'salary_steps'

    id = Column(Integer, primary_key=True)
    name = Column(String(191), nullable=False)
    salary_structure_id = Column(ForeignKey('salary_structures.id'), index=True, server_default=FetchedValue())
    salary_grade_id = Column(ForeignKey('salary_grades.id'))
    salary = Column(Float(asdecimal=True), default=0)
    description = Column(String(700))
    created_at = Column(DateTime, default=datetime.utcnow())
    updated_at = Column(DateTime, default=datetime.utcnow())
    deleted_at = Column(DateTime, nullable=True, default=False)

    salary_structure = relationship('SalaryStructure',
                                    primaryjoin='SalaryStep.salary_structure_id == SalaryStructure.id',
                                    # backref='salary_steps'
                                    )
    salary_grade = relationship('SalaryGrade',
                                primaryjoin='SalaryStep.salary_grade_id == SalaryGrade.id',
                                # backref='salary_steps'
                                )

    def __repr__(self):
        return self.name
