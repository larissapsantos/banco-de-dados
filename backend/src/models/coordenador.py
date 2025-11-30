from sqlalchemy import create_engine, Column, Integer, String,ForeignKey
from sqlalchemy_utils.types import ChoiceType
from sqlalchemy import text
from src.database import Base

class Coordenador(Base):
        __tablename__ = "coordenador"
        SITUACAO_COORDENADOR =(
        ("ATIVO", "ATIVO"), 
        ("INATIVO", "INATIVO")
    )

        matricula = Column("matricula", Integer, primary_key=True)
        nome = Column("nome", String)
        situacao = Column("situacao", ChoiceType        (choices=SITUACAO_COORDENADOR))
        id_escola = Column("id", ForeignKey("escola.id"))