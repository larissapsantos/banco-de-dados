from sqlalchemy import create_engine, Column, String, Date, Integer, ForeignKey
from sqlalchemy import text
from sqlalchemy_utils.types import ChoiceType
from src.database import Base

class Equipamento(Base):
    __tablename__ = "equipamento"

    STATUS_EQUIPAMENTOS = (
        ("DISPONÍVEL", "DISPONÍVEL"), 
        ("INDISPONÍVEL", "INDISPONÍVEL")
        )

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    descricao = Column("descricao", String)
    nome = Column("nome", String)
    localizacao = Column("localizacao", String)
    condicao = Column("condicao", String)
    data_compra = Column("data_compra", Date)
    status = Column("status", ChoiceType(choices=STATUS_EQUIPAMENTOS), default="DISPONÍVEL")

    id_fabricante = Column("id_fabricante", ForeignKey("fabricante.cnpj"))
    id_categoria = Column("id_categoria", ForeignKey("categoria.id"))