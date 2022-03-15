from flask_appbuilder import Model
from sqlalchemy import (BigInteger, Boolean, Column, Date, Integer, String, text)
from sqlalchemy.dialects.postgresql.base import UUID
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class Employees(Model):
    __tablename__ = 'employees'

    id = Column(BigInteger, primary_key=True)
    uuid = Column(UUID, nullable=False)
    user_id = Column(Integer, server_default=text("0"))
    first_name = Column(String(255))
    last_name = Column(String(255))
    other_names = Column(String(255))
    gender_id = Column(Integer, server_default=text("0"))
    date_of_birth = Column(Date)
    state_of_origin_id = Column(Integer, server_default=text("0"))
    lga_of_origin_id = Column(Integer, server_default=text("0"))
    ippis_id = Column(String(255), unique=True)
    employee_number = Column(String(255))
    income_tax_provider_id = Column(Integer, server_default=text("0"))
    tin = Column(String(255))
    pencon_provider_id = Column(Integer, server_default=text("0"))
    pencon_id = Column(String(255))
    nhis_provider_id = Column(Integer, server_default=text("0"))
    nhis_id = Column(String(255))
    nhf_provider_id = Column(Integer, server_default=text("0"))
    nhf_id = Column(String(255))
    mda_id = Column(Integer, server_default=text("0"))
    section_id = Column(Integer, server_default=text("0"))
    # created_by = Column(Integer, server_default=text("0"))
    # deleted_by = Column(Integer, server_default=text("0"))
    # created_at = Column(DateTime)
    # updated_at = Column(DateTime)
    # deleted_at = Column(DateTime)
    verified_pencon_id = Column(Boolean, nullable=False, server_default=text("false"))

    def __repr__(self):
        return self.name
