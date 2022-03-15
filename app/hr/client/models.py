# import datetime as date
from datetime import datetime
import uuid
from flask_appbuilder import Model
from sqlalchemy import (BigInteger, Boolean, Column, Date, DateTime, ForeignKey, Index, Integer, Numeric, SmallInteger,
                        String, Table, Text, text)
from sqlalchemy.dialects.postgresql.base import INET, UUID
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy_utils.types.uuid import UUIDType

from etas.app.models import BaseModel as Model


class ClientType(Model):
    __tablename__ = 'client_types'

    id = Column(Integer, unique=True, primary_key=True)
    name = Column(String(191), nullable=False)

    description = Column(Text())

    def __repr__(self):
        return self.name


class ClientGroup(Model):
    __tablename__ = 'client_groups'

    id = Column(Integer, unique=True, primary_key=True)
    name = Column(String(191), nullable=False)

    client_group_id = Column(Integer, ForeignKey("client_types.id"), default=0)
    client_group = relationship("ClientType")

    description = Column(Text())

    def __repr__(self):
        return self.name


class Client(Model):
    __tablename__ = 'clients'

    id = Column(BigInteger, primary_key=True)
    uuid = Column(UUIDType(binary=False), default=uuid.uuid4, primary_key=True)
    name = Column(String(191), unique=True, nullable=False)
    short_name = Column(String(255))

    client_group_id = Column(Integer, ForeignKey("client_groups.id"), default=0)
    client_group = relationship("ClientGroup")

    client_type_id = Column(Integer, ForeignKey("client_types.id"), default=0)
    client_type = relationship("ClientType")

    company_name = Column(String(255))
    cac_reg_no = Column(String(255))
    tax_id = Column(String(255))
    tax_state_id = Column(Integer, server_default=text("0"))
    address = Column(Text)
    street = Column(Text)
    state_id = Column(Integer, nullable=False, server_default=text("0"))
    state_lga_id = Column(Integer, nullable=False, server_default=text("0"))
    contact_name = Column(String(255))
    contact_phone = Column(String(255))
    contact_email = Column(String(255))
    website = Column(String(255))
    bank_id = Column(Integer, nullable=False, server_default=text("0"))
    bank_account = Column(String(255))
    code = Column(String(255))

    note = Column(Text())

    def __repr__(self):
        return self.name
