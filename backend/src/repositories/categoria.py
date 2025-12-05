from sqlalchemy.orm import Session
from sqlalchemy import text

class CategoriaRepos:
    def listar(self, db: Session):
        sql = text("SELECT * FROM categoria")
        result = db.execute(sql).mappings().all()   # retorna dicts
        return result
    
    def buscar_por_id(self, db: Session, id: int):
        sql = text("""
            SELECT * FROM categoria
            WHERE id = :id
            LIMIT 1
        """)
        result = db.execute(sql, {"id": id}).mappings().first()
        return result