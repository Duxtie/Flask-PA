import datetime

import uuid
from flask_appbuilder.security.sqla.models import User
from sqlalchemy import Column, Date, ForeignKey, Integer, String, DateTime
# from sqlalchemy.ext.declarative import declared_attr
from sqlalchemy.orm import relationship
from sqlalchemy.schema import FetchedValue
# from payroll_analysis.app.hr.company.models import Company
# from ...hr.company.models import Company
# from ...biodata.gender.models import Gender

mindate = datetime.date(datetime.MINYEAR, 1, 1)


class ACLUser(User):
    __tablename__ = "ab_user"

    # uuid = Column(String(36), unique=True, index=True, nullable=False, server_default=str(uuid.uuid4()))

    phone = Column(String(191), unique=True)
    middle_name = Column(String(191), server_default=FetchedValue())

    # gender_id = Column(Integer, ForeignKey("genders.id"), nullable=True, default=0)
    # gender = relationship(Gender)

    date_of_birth = Column(Date)
    avatar = Column(String(255))

    last_ip = Column(String(40))
    last_login_at = Column(DateTime)

    last_password_change = Column(DateTime)

    new_pass_key = Column(String(32))
    new_pass_key_requested = Column(DateTime)

    is_active = Column(Integer, nullable=False, default=1)

    two_factor_auth_enabled = Column(Integer, default=0)
    two_factor_auth_code = Column(String(100))
    two_factor_auth_code_requested = Column(DateTime)

    def __repr__(self):
        return self.get_full_name()

    def created_at(self):
        return self.created_on

    def updated_at(self):
        return self.changed_on

    def status(self):
        return self.is_active
