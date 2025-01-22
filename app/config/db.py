import os
from sqlalchemy import create_engine
from sqlalchemy.orm.session import sessionmaker
from sqlalchemy.orm import declarative_base
"""
en este modulo se crea el archivo, teniendo en cuenta los 
modeles creados en paquete de models, con este creanis la base
con sqlalchemy
"""

sqlite_file_name = "../database.sqlite"
base_dir = os.path.dirname(os.path.realpath(__file__))


database_url = f"sqlite:///{os.path.join(base_dir, sqlite_file_name)}"
engine = create_engine(database_url, echo=True)


Session = sessionmaker(bind=engine)
Base = declarative_base()
