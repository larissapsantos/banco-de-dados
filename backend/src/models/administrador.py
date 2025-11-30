from sqlalchemy import create_engine, Column, Integer, String, Date
from sqlalchemy import text
from src.database import Base

class Administrador(Base):
    __tablename__ = "administrador"

    matricula = Column("matricula", Integer, primary_key=True)
    nome = Column("nome", String(100))
    email = Column("email", String(100))
    bairro = Column("bairro", String(100))
    uf = Column("uf", String(2))