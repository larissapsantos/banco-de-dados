from src.models.fabricante import Fabricante
from sqlalchemy.orm import Session

class FabricanteRepos:
    def listar(self, bd: Session):
        return bd.query(Fabricante).all()
    
    def buscar_por_id(self, db: Session, id: int):
        return db.query(Fabricante).filter(Fabricante.id == id).first()