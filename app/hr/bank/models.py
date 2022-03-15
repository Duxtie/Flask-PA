# import datetime as date
from datetime import datetime

from flask_appbuilder import Model
from sqlalchemy import (BigInteger, Boolean, Column, Date, DateTime, ForeignKey, Index, Integer, Numeric, SmallInteger,
                        String, Table, Text, text)
from sqlalchemy.dialects.postgresql.base import INET, UUID
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

from etas.app.models import BaseModel as Model


class BankType(Model):
    __tablename__ = 'bank_types'

    id = Column(BigInteger, primary_key=True, server_default=text("nextval('bank_types_id_seq'::regclass)"))
    name = Column(String(255), nullable=False)
    short_name = Column(String(255))
    code = Column(String(255))
    is_active = Column(Boolean, nullable=False, server_default=text("true"))
    description = Column(Text)

    def __repr__(self):
        return self.name


class Bank(Model):
    __tablename__ = 'banks'

    id = Column(BigInteger, primary_key=True, server_default=text("nextval('banks_id_seq'::regclass)"))
    uuid = Column(UUID)
    name = Column(String(191), unique=True, nullable=False)
    code = Column(String(255))
    short_name = Column(String(255))

    bank_type_id = Column(Integer, ForeignKey("bank_types.id"), default=0)
    bank_type = relationship("BankType")

    note = Column(Text())

    def __repr__(self):
        return self.name
