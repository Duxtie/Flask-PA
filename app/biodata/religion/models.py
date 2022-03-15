from flask_appbuilder import Model
from sqlalchemy import Column, Integer, String, Text


class Religion(Model):
    __tablename__ = 'religions'

    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True, nullable=False)
    description = Column(Text)

    def __repr__(self):
        return self.name
