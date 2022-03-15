from flask_appbuilder import Model
from sqlalchemy import Column, Integer, String


class Designations(Model):
    __tablename__ = 'designations'

    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True, nullable=False)

    def __repr__(self):
        return self.name
