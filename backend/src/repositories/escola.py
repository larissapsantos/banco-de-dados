from src.models.escola import Escola
from sqlalchemy.orm import Session

class EscolaRepos:
    def listar(self, db: Session):
        return db.query(Escola).all()
    
    def buscar_por_id(self, db: Session, id: int):
        return db.query(Escola).filter(Escola.id == id).first()