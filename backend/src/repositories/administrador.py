from sqlalchemy.orm import Session
from sqlalchemy import text

class AdministradorRepo:
    def listar(self, db: Session):
        sql = text("SELECT * FROM administrador")
        result = db.execute(sql).mappings().all()   # retorna dicts
        return result
    
    def buscar_por_id(self, db: Session, id: int):
        sql = text("""
            SELECT * FROM administrador
            WHERE matricula = :matricula
            LIMIT 1
        """)
        result = db.execute(sql, {"matricula": id}).mappings().first()
        return result