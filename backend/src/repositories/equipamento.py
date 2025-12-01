from src.models.equipamento import Equipamento
from sqlalchemy.orm import Session

class EquipamentoRepos:
    def listar(self, db: Session):
        return db.query(Equipamento).all()
    
    def buscar_por_id(self, db: Session, id: int):
        return db.query(Equipamento).filter(Equipamento.id == id).first()