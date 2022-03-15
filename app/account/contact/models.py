import datetime
import uuid

from flask_appbuilder import Model
from flask_appbuilder.models.mixins import FileColumn
from sqlalchemy import (BigInteger, Boolean, Column, Date, DateTime, ForeignKey, Index, Integer, Numeric, SmallInteger, String, Table, Text, text)
from sqlalchemy.dialects.postgresql.base import INET, UUID
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base


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

    Column('id', UUID, nullable=False),
    Column('reference_id', String(255), nullable=False, unique=True),

    contact_status_id = Column(ForeignKey('contact_status.id'), default=1000)
    contact_status = relationship(ContactStatus)

    Column('company_name', String(255)),
    Column('cac_reg_no', String(255)),
    Column('client_type_id', Integer, nullable=False, server_default=text("0")),
    Column('tax_id', String(255)),
    Column('tax_state_id', Integer, server_default=text("0")),
    Column('address', Text),
    Column('street', Text),
    Column('state_id', Integer, nullable=False, server_default=text("0")),
    Column('state_lga_id', Integer, nullable=False, server_default=text("0")),
    Column('contact_name', String(255)),
    Column('contact_phone', String(255)),
    Column('contact_email', String(255)),
    Column('website', String(255)),
    Column('bank_id', Integer, nullable=False, server_default=text("0")),
    Column('bank_account', String(255)),
    Column('code', String(255), unique=True),

    def __repr__(self):
        return self.full_name()

    def full_name(self):
        return '{} {} {}'.format(self.last_name, self.first_name, self.middle_name)
