from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy import text
from sqlalchemy_utils.types import ChoiceType
from src.database import Base

class Categoria(Base):
    __tablename__ = "Categoria"
    CATEGORIA_EQUIPAMENTO =(
        ("IMPRESSORA 3D", "IMPRESSORA 3D"), 
        ("MATERIAL", "MATERIAL"),
        ("KIT ROBÓTICA", "KIT ROBÓTICA")
    )

    id = Column("id", Integer, primary_key=True)
    nome = Column("nome", String)
    descricao = Column("descricao", ChoiceType(choices=CATEGORIA_EQUIPAMENTO))