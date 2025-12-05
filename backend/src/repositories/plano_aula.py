from sqlalchemy.orm import Session
from sqlalchemy import text
from typing import List, Dict, Optional

class PlanoAulaRepos:

    def criar(self, db: Session, plano: dict) -> Optional[Dict]:
        sql = text("""
            INSERT INTO plano_aula (titulo, descricao, status, id_professor, id_coordenador)
            VALUES (:titulo, :descricao, :status, :id_professor, :id_coordenador)
        """)
        try:
            db.execute(sql, plano)
            db.commit()
            return {}
        except Exception as e:
            db.rollback()
            print(f"Erro ao criar plano de aula: {e}")
            return None

    def listar(self, db: Session) -> List[Dict]:
        sql = text("SELECT * FROM plano_aula ORDER BY id")
        return db.execute(sql).mappings().all()
    
    def buscar_por_id(self, db: Session, id: int) -> Optional[Dict]:
        sql = text("""
            SELECT * FROM plano_aula
            WHERE id = :id
            LIMIT 1
        """)
        return db.execute(sql, {"id": id}).mappings().first()
    
    def listar_por_professor(self, db: Session, id_professor: int) -> List[Dict]:
        sql = text("""
            SELECT * FROM plano_aula
            WHERE id_professor = :id_professor
            ORDER BY id
        """)
        return db.execute(sql, {"id_professor": id_professor}).mappings().all()

    def listar_por_escola(self, db: Session, id_escola: int) -> List[Dict]:
        sql = text("""
            SELECT p.*, prof.nome AS nome_professor
            FROM plano_aula p
            JOIN professor prof ON prof.matricula = p.id_professor
            WHERE prof.id_escola = :id_escola
            ORDER BY p.id
        """)
        return db.execute(sql, {"id_escola": id_escola}).mappings().all()

    def listar_pendentes_por_bairro(self, db: Session, bairro: str) -> List[Dict]:
        sql = text("""
            SELECT *
            FROM vw_plano_aula_com_professor
            WHERE REPLACE(LOWER(bairro_escola), ' ', '')
            LIKE CONCAT('%', REPLACE(LOWER(:bairro), ' ', ''), '%')
        """)
        return db.execute(sql, {"bairro": bairro}).mappings().all()

    def editar(self, db: Session, id: int, novos_dados: dict) -> Optional[Dict]:
        campos_permitidos = ["titulo", "descricao", "status"]
        atualizacoes = {}

        for campo in campos_permitidos:
            if campo in novos_dados:
                atualizacoes[campo] = novos_dados[campo]

        if not atualizacoes:
            return self.buscar_por_id(db, id)

        atualizacoes["id"] = id
        set_clause = ", ".join([f"{campo} = :{campo}" for campo in atualizacoes if campo != "id"])

        sql = text(f"""
            UPDATE plano_aula
            SET {set_clause}
            WHERE id = :id
        """)
        try:
            db.execute(sql, atualizacoes)
            sql_select = text(f"""
                SELECT id, titulo, descricao, status FROM plano_aula
                WHERE id = :id
            """)
            result = db.execute(sql_select, atualizacoes).mappings().first()
            db.commit()
            return result
        except Exception as e:
            db.rollback()
            print(f"Erro ao editar plano de aula {id}: {e}")
            return None

    def deletar(self, db: Session, id: int) -> bool:
        sql = text("""
            DELETE FROM plano_aula
            WHERE id = :id
        """)
        try:
            result = db.execute(sql, {"id": id})
            db.commit()
            return result.rowcount > 0
        except Exception as e:
            db.rollback()
            print(f"Erro ao excluir plano de aula {id}: {e}")
            return False