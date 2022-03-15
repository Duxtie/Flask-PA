from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from flask_appbuilder import Model


class State(Model):
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True, nullable=False)

    def __repr__(self):
        return self.name


class LGA(Model):
    __tablename__ = 'state_lgas'

    id = Column(Integer, primary_key=True)
    name = Column(String(191), nullable=False)

    state_id = Column(Integer, ForeignKey("states.id"), default=0)
    state = relationship("State")

    def __repr__(self):
        return self.name
