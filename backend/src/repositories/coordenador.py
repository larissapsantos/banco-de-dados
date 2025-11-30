from src.models.coordenador import Coordenador
from sqlalchemy.orm import Session

class CoordenadorRepos:
    def listar(self, bd: Session):
        return bd.query(Coordenador).all()
    
    def buscar_por_id(self, db: Session, id: int):
        return db.query(Coordenador).filter(Coordenador.id == id).first()