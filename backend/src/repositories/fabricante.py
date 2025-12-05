from sqlalchemy.orm import Session
from sqlalchemy import text
from typing import List, Dict, Optional

class FabricanteRepos:
    def listar(self, db: Session) -> List[Dict]:
        sql = text("SELECT * FROM fabricante ORDER BY nome")
        result = db.execute(sql).mappings().all()
        return result
    
    def buscar_por_cnpj(self, db: Session, cnpj: str) -> Optional[Dict]:
        sql = text("SELECT * FROM fabricante WHERE cnpj = :cnpj")
        result = db.execute(sql, {"cnpj": cnpj}).mappings().first()
        return result