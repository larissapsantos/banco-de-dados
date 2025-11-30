from pymysql import Date
from sqlalchemy import create_engine, Column, Integer, Date, String
from sqlalchemy_utils.types import ChoiceType
from sqlalchemy import text
from src.database import Base

class Professor(Base):
    __tablename__ = "professor"
    SITUACAO_PROFESSOR =(
        ("ATIVO", "ATIVO"), 
        ("INATIVO", "INATIVO")
    )

    matricula = Column("matricula", Integer, primary_key=True)
    nome = Column("nome", String)
    situacao = Column("situacao", ChoiceType(choices=SITUACAO_PROFESSOR))
    id_escola = Column("id_escola", Integer)