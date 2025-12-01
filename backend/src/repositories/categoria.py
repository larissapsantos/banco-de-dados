from src.models.categoria import Categoria
from sqlalchemy.orm import Session

class CategoriaRepos:
    def listar(self, db: Session):
        return db.query(Categoria).all()
    
    def buscar_por_id(self, db: Session, id: int):
        return db.query(Categoria).filter(Categoria.id == id).first()