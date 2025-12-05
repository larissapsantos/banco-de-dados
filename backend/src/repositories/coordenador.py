from typing import List, Dict, Optional
from sqlalchemy.orm import Session
from sqlalchemy import text

class CoordenadorRepos:
    def listar(self, db: Session) -> List[Dict]:
        sql = text("SELECT * FROM coordenador ORDER BY matricula")
        result = db.execute(sql).mappings().all()
        return result
    
    def buscar_por_matricula(self, db: Session, matricula: int) -> Optional[Dict]:
        sql = text("""
            SELECT * FROM coordenador
            WHERE matricula = :matricula
        """)
        result = db.execute(sql, {"matricula": matricula}).mappings().first()
        return result
    
    def buscar_por_id(self, db: Session, id: int) -> Optional[Dict]:
        return self.buscar_por_matricula(db, id)
    
    def buscar_por_escola(self, db: Session, id_escola: int) -> List[Dict]:
        sql = text("""
            SELECT * FROM coordenador
            WHERE id_escola = :id_escola
            ORDER BY matricula
        """)
        result = db.execute(sql, {"id_escola": id_escola}).mappings().all()
        return result
    
    def buscar_coordenador_principal_escola(self, db: Session, id_escola: int) -> Optional[Dict]:
        sql = text("""
            SELECT * FROM coordenador
            WHERE id_escola = :id_escola
            LIMIT 1
        """)
        result = db.execute(sql, {"id_escola": id_escola}).mappings().first()
        return result