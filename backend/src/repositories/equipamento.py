from src.models.equipamento import Equipamento
from sqlalchemy.orm import Session

class EquipamentoRepos:
    def listar(self, bd: Session):
        return bd.query(Equipamento).all()
    
    def buscar_por_id(self, db: Session, id: int):
        return db.query(Equipamento).filter(Equipamento.id == id).first()