# import datetime as date
from datetime import datetime

from flask_appbuilder import Model
from sqlalchemy import Column, DateTime, Integer, String, ForeignKey, Text

from etas.app.models import BaseModel as Model
from sqlalchemy.orm import relationship


class CompanyGroup(Model):
    __tablename__ = 'company_groups'

    id = Column(Integer, unique=True, primary_key=True)
    name = Column(String(191), nullable=False)
    description = Column(Text())

    def __repr__(self):
        return self.name


class Company(Model):
    __tablename__ = 'companies'

    id = Column(Integer, primary_key=True)
    name = Column(String(191), unique=True, nullable=False)
    note = Column(Text())

    company_group_id = Column(Integer, ForeignKey("company_groups.id"), default=0)
    company_group = relationship("CompanyGroup")

    def __repr__(self):
        return self.name
