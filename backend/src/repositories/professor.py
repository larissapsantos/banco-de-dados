from src.models.professor import Professor
from sqlalchemy.orm import Session

class ProfessorRepos:
    def listar(self, bd: Session):
        return bd.query(Professor).all()
    
    def buscar_por_id(self, db: Session, id: int):
        return db.query(Professor).filter(Professor.id == id).first()