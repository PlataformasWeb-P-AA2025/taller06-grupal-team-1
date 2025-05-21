from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from generar_base import Pais
import requests

# URL del JSON
url = 'https://pkgstore.datahub.io/core/country-codes/country-codes_json/data/616b1fb83cbfd4eb6d9e7d52924bb00a/country-codes_json.json'

# Obtener datos
response = requests.get(url)
datos = response.json()

# Conexión a la base de datos
engine = create_engine('sqlite:///basedatos_paises.db')
Session = sessionmaker(bind=engine)
session = Session()

# Insertar cada país
for item in datos:
    pais = Pais(
        nombre_pais = item.get("CLDR display name"),
        capital = item.get("Capital"),
        continente = item.get("Continent"),
        dial = item.get("Dial"),
        geoname_id = int(item["Geoname ID"]) if item.get("Geoname ID") else None,
        itu = item.get("ITU"),
        lenguajes = item.get("Languages"),
        es_independiente = item.get("is_independent")
    )
    session.add(pais)

# Confirmar cambios
session.commit()

