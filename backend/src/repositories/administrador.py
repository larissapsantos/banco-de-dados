from src.models.administrador import Administrador
from sqlalchemy.orm import Session

class EquipamentoRepos:
    def listar(self, bd: Session):
        return bd.query(Administrador).all()
    
    def buscar_por_id(self, db: Session, id: int):
        return db.query(Administrador).filter(Administrador.id == id).first()