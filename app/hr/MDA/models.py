# import datetime as date
from datetime import datetime

from flask_appbuilder import Model
from sqlalchemy import (BigInteger, Boolean, Column, Date, DateTime, ForeignKey, Index, Integer, Numeric, SmallInteger,
                        String, Table, Text, text)
from sqlalchemy.dialects.postgresql.base import INET, UUID
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

from etas.app.models import BaseModel as Model


class MDAType(Model):
    __tablename__ = 'mda_types'

    id = Column(Integer, unique=True, primary_key=True)
    name = Column(String(191), nullable=False)
    short_name = Column(String(255))
    code = Column(String(255))

    description = Column(Text())

    def __repr__(self):
        return self.name


class MDAGroup(Model):
    __tablename__ = 'mda_groups'

    id = Column(Integer, unique=True, primary_key=True)
    name = Column(String(191), nullable=False)
    short_name = Column(String(255))
    code = Column(String(255))

    mda_type_id = Column(Integer, ForeignKey("mda_types.id"), default=0)
    mda_type = relationship("MDAType")

    description = Column(Text())

    def __repr__(self):
        return self.name


class MDA(Model):
    __tablename__ = 'mdas'

    id = Column(BigInteger, primary_key=True)
    uuid = Column(UUID)
    name = Column(String(191), unique=True, nullable=False)
    short_name = Column(String(255))

    mda_group_id = Column(Integer, ForeignKey("mda_groups.id"), default=0)
    mda_group = relationship("MDAGroup")

    mda_type_id = Column(Integer, ForeignKey("mda_types.id"), default=0)
    mda_type = relationship("MDAType")

    code = Column(String(255))

    note = Column(Text())

    def __repr__(self):
        return self.name
