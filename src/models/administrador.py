from sqlalchemy import create_engine, Column, Integer, String, Date
from sqlalchemy import text
from src.database import Base

class Administrador(Base):
    __tablename__ = "servidor_adm"

    matricula = Column("matricula", Integer, primary_key=True)
    nome = Column("nome", String)
    email = Column("email", String)
    bairro = Column("bairro", String)
    uf = Column("uf", String)