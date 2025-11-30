from sqlalchemy import DateTime, create_engine, Column, Integer, Date, Time, ForeignKey
from sqlalchemy import text
from src.database import Base

class Emprestimo(Base):
        __tablename__ = "emprestimo"

        id = Column("id", Integer, primary_key=True, autoincrement=True)
        quantidade = Column("quantidade", Integer, nullable=False)
        data_hora = Column("data_hora", DateTime)
        id_escola = Column(Integer, ForeignKey("escola.id"), nullable=False)
        id_equipamento = Column(Integer, ForeignKey("equipamento.id"), nullable=False)
        id_plano_aula = Column(Integer,ForeignKey("plano_aula.id"), nullable=False)

        def __init__(self, quantidade, id_escola, id_equipamento, id_plano_aula):
            self.quantidade = quantidade 
            self.id_escola = id_escola 
            self.id_equipamento = id_equipamento 
            self.id_plano_aula = id_plano_aula