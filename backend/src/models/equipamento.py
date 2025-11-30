from sqlalchemy import create_engine, Column, String, Date, Integer, ForeignKey
from sqlalchemy import text
from src.database import Base

class Equipamento(Base):
    __tablename__ = "equipamento"


    id = Column("id", Integer, primary_key=True, autoincrement=True)
    descricao = Column("descricao", String(300))
    nome = Column("nome", String(100))
    localizacao = Column("localizacao", String(100))
    condicao = Column("condicao", String(50))
    data_compra = Column("data_compra", Date)
    status = Column("status", String(50))
    id_fabricante = Column("id_fabricante", ForeignKey("fabricante.cnpj"))
    id_categoria = Column("id_categoria", ForeignKey("categoria.id"))