from database import Base
from sqlalchemy import Column, Integer, String, ForeignKey

class Vaccination(Base):
    __tablename__ = "vaccinationpoints"
    id = Column(Integer, primary_key=True)
    local = Column(String)
    atendimento = Column(String)
    publico = Column(String)

class City(Base):
    __tablename__ = "cities"
    id = Column(Integer, primary_key=True)
    name = Column(String)