from flask_appbuilder import Model
from sqlalchemy import Column, Integer, String, Text, Float


class Country(Model):
    __tablename__ = 'countries'

    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True, nullable=False)
    area = Column(Integer)
    cioc = Column(String(5), unique=True)
    cca2 = Column(String(5), unique=True)
    capital = Column(String(50))
    lat = Column(Float)
    lng = Column(Float)
    cca3 = Column(String(5), unique=True)
    note = Column(Text)

    def __repr__(self):
        return self.name
