import datetime
import logging

from flask import g
from flask_appbuilder import Model
# from flask_appbuilder.models.mixins import AuditMixin
from sqlalchemy import Column, DateTime, ForeignKey, Integer, Boolean, text
from sqlalchemy.ext.declarative import declared_attr
from sqlalchemy.orm import relationship

try:
    from sqlalchemy.ext.declarative import as_declarative
except ImportError:
    from sqlalchemy.ext.declarative.api import as_declarative

log = logging.getLogger(__name__)

"""

You can use the extra Flask-AppBuilder fields and Mixin's

AuditMixin will add automatic timestamp of created and modified by who


"""


class BaseAuditMixin(object):
    """
        AuditMixin
        Mixin for models, adds 4 columns to stamp,
        time and user on creation and modification
        will create the following columns:

        :created on:
        :changed on:
        :created by:
        :changed by:
    """

    created_at = Column(DateTime, default=datetime.datetime.now, nullable=False)
    updated_at = Column(
        DateTime,
        default=datetime.datetime.now,
        onupdate=datetime.datetime.now,
        nullable=False,
    )
    deleted_at = Column(DateTime, nullable=True, default=False)

    @declared_attr
    def created_by_fk(cls):
        return Column(
            Integer, ForeignKey("ab_user.id"), default=cls.get_user_id, nullable=False
        )

    @declared_attr
    def created_by(cls):
        return relationship(
            "User",
            primaryjoin="%s.created_by_fk == User.id" % cls.__name__,
            enable_typechecks=False,
        )

    @declared_attr
    def changed_by_fk(cls):
        return Column(
            Integer,
            ForeignKey("ab_user.id"),
            default=cls.get_user_id,
            onupdate=cls.get_user_id,
            nullable=False,
        )

    @declared_attr
    def changed_by(cls):
        return relationship(
            "User",
            primaryjoin="%s.changed_by_fk == User.id" % cls.__name__,
            enable_typechecks=False,
        )

    @classmethod
    def get_user_id(cls):
        try:
            return g.user.id
        except Exception:
            return None


# @as_declarative(name="BaseModel", metaclass=ModelDeclarativeMeta)
class BaseModel(Model):
    __abstract__ = True

    _audit_mixin_ = True

    is_active = Column(Boolean, nullable=False, server_default=text("true"))

    """
        BaseModel (AuditMixin)
        Mixin for models, adds 5 columns to stamp,
        time and user on creation and modification
        will create the following columns:

        :is active:
        :created on:
        :changed on:
        :created by:
        :changed by:
    """

    if _audit_mixin_:
        created_at = Column(DateTime, default=datetime.datetime.now, nullable=False)
        updated_at = Column(
            DateTime,
            default=datetime.datetime.now,
            onupdate=datetime.datetime.now,
            nullable=False,
        )
        deleted_at = Column(DateTime, nullable=True)

    @declared_attr
    def created_by_fk(cls):
        if cls._audit_mixin_:
            return Column(
                Integer, ForeignKey("ab_user.id"), default=cls.get_user_id, nullable=False
            )

    @declared_attr
    def created_by(cls):
        if cls._audit_mixin_:
            return relationship(
                "User",
                primaryjoin="%s.created_by_fk == User.id" % cls.__name__,
                enable_typechecks=False,
            )

    @declared_attr
    def updated_by_fk(cls):
        if cls._audit_mixin_:
            return Column(
                Integer,
                ForeignKey("ab_user.id"),
                default=cls.get_user_id,
                onupdate=cls.get_user_id,
                nullable=False,
            )

    @declared_attr
    def updated_by(cls):
        if cls._audit_mixin_:
            return relationship(
                "User",
                primaryjoin="%s.updated_by_fk == User.id" % cls.__name__,
                enable_typechecks=False,
            )

    @classmethod
    def get_user_id(cls):
        if cls._audit_mixin_:
            try:
                return g.user.id
            except Exception:
                return None

