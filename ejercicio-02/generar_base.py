from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

# Crear motor para SQLite
engine = create_engine('sqlite:///basedatos_paises.db')
Base = declarative_base()

# Crear entidad País
class Pais(Base):
    __tablename__ = 'paises'

    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre_pais = Column(String)
    capital = Column(String)
    continente = Column(String)
    dial = Column(String)
    geoname_id = Column(Integer)
    itu = Column(String)
    lenguajes = Column(String)
    es_independiente = Column(String)

# Crear todas las tablas
Base.metadata.create_all(engine)

