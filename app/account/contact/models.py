import datetime
import uuid

from flask_appbuilder import Model
from flask_appbuilder.models.mixins import FileColumn
from sqlalchemy import (BigInteger, Boolean, Column, Date, DateTime, ForeignKey, Index, Integer, Numeric, SmallInteger,
                        String, Table, Text, text)
from sqlalchemy.dialects.postgresql.base import INET, UUID
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy_utils.types.uuid import UUIDType

from ...biodata.gender.models import Gender
from ...biodata.title.models import Title
from ...hr.designation.models import Designation

from etas.app.models import BaseModel

# from flask import g
# from flask_uuid import FlaskUUID
# from etas.app.platform.acl.models import ACLUser as User

mindate = datetime.date(datetime.MINYEAR, 1, 1)


class ContactStatus(Model):
    __tablename__ = 'contact_status'

    _audit_mixin_ = False

    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True, nullable=False)

    def __repr__(self):
        return self.name


class Contact(BaseModel):
    __tablename__ = 'contacts'

    id = Column(UUIDType(binary=False), default=uuid.uuid4, primary_key=True)

    contact_status_id = Column(ForeignKey('contact_status.id'), default=1000)
    contact_status = relationship(ContactStatus)

    first_name = Column(String(50))
    last_name = Column(String(50))
    middle_name = Column(String(50))
    date_of_birth = Column(Date)

    gender_id = Column(ForeignKey('genders.id'), default=9)
    gender = relationship(Gender, foreign_keys=[gender_id])

    designation_id = Column(ForeignKey('designations.id'), default=1000)
    designation = relationship(Designation)

    title_id = Column(ForeignKey('titles.id'), default=1000)
    title = relationship(Title)

    def __repr__(self):
        return self.full_name()

    def full_name(self):
        return '{} {} {}'.format(self.last_name, self.first_name, self.middle_name)
