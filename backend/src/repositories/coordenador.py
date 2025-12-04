from src.models.coordenador import Coordenador
from sqlalchemy.orm import Session

class CoordenadorRepos:
    def listar(self, db: Session):
        return db.query(Coordenador).all()
    
    def buscar_por_id(self, db: Session, id: int):
        return db.query(Coordenador).filter(Coordenador.matricula == id).first()
    
    def buscar_por_escola(self, db: Session, id_escola: int):
        return db.query(Coordenador).filter(Coordenador.id_escola == id_escola).first()