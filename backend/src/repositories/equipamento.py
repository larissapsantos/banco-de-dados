from sqlalchemy.orm import Session
from sqlalchemy import text

class EquipamentoRepos:
    
    def listar(self, db: Session):
        sql = text("SELECT * FROM equipamento ORDER BY id")
        result = db.execute(sql).mappings().all()
        return result
    
    def buscar_por_id(self, db: Session, id: int):
        sql = text("""
            SELECT * FROM equipamento
            WHERE id = :id
            LIMIT 1
        """)
        result = db.execute(sql, {"id": id}).mappings().first()
        return result