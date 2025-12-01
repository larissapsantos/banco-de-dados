from src.models.administrador import Administrador
from sqlalchemy.orm import Session

class AdministradorRepo:
    def listar(self, db: Session):
        return db.query(Administrador).all()
    
    def buscar_por_id(self, db: Session, id: int):
        return db.query(Administrador).filter(Administrador.matricula == id).first()