from src.models.professor import Professor
from sqlalchemy import text
from sqlalchemy.orm import Session
from typing import List, Dict, Optional

class ProfessorRepos:
    def listar(self, db: Session) -> List[Dict]:
        sql = text("SELECT * FROM professor ORDER BY nome")
        return db.execute(sql).mappings().all()
    
    def buscar_por_id(self, db: Session, id: int) -> Optional[Dict]:
        sql = text("SELECT * FROM professor WHERE matricula = :matricula")
        return db.execute(sql, {"matricula": id}).mappings().first()