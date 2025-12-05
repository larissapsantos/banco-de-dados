from sqlalchemy.orm import Session
from sqlalchemy import text
from typing import List, Dict, Optional

class SolicitacaoRepos:

    def criar(self, db: Session, solicitacao: dict) -> Optional[Dict]:
        sql = text("""
            CALL sp_criar_solicitacao (
                :id_servidor,
                :id_emprestimo,
                :id_coordenador
            )
        """)
        try:
            result = db.execute(sql, solicitacao).mappings().first()
            db.commit()
            return result
        except Exception as e:
            db.rollback()
            print(f"Erro ao criar solicitação: {e}")
            return None

    def listar(self, db: Session) -> List[Dict]:
        sql = text("SELECT * FROM solicitacao ORDER BY id_servidor, id_emprestimo, id_coordenador")
        return db.execute(sql).mappings().all()

    def buscar_por_chave_composta(
        self, db: Session, id_servidor: int, id_emprestimo: int, id_coordenador: int
    ) -> Optional[Dict]:
        sql = text("""
            SELECT *
            FROM solicitacao
            WHERE id_servidor = :id_servidor
              AND id_emprestimo = :id_emprestimo
              AND id_coordenador = :id_coordenador
            LIMIT 1
        """)
        params = {
            "id_servidor": id_servidor,
            "id_emprestimo": id_emprestimo,
            "id_coordenador": id_coordenador
        }

        return db.execute(sql, params).mappings().first()

    def editar(self, db: Session, id_servidor: int, id_emprestimo: int, id_coordenador: int, novos_dados: dict) -> Optional[Dict]:
        if "status" not in novos_dados:
            return self.buscar_por_chave_composta(db, id_servidor, id_emprestimo, id_coordenador)

        sql = text("""
            UPDATE solicitacao
            SET status = :status
            WHERE id_servidor = :id_servidor
              AND id_emprestimo = :id_emprestimo
              AND id_coordenador = :id_coordenador
        """)

        params = {
            "id_servidor": id_servidor,
            "id_emprestimo": id_emprestimo,
            "id_coordenador": id_coordenador,
            "status": novos_dados["status"]
        }
        try:
            db.execute(sql, params)
            sql_select = text("""
                SELECT * FROM solicitacao WHERE id_servidor = :id_servidor AND id_emprestimo = :id_emprestimo AND id_coordenador = :id_coordenador
            """)
            result = db.execute(sql_select, params).mappings().first()
            db.commit()
            return result
        except Exception as e:
            db.rollback()
            print(f"Erro ao editar solicitacao: {e}")
            return None

    def deletar(self, db: Session, id_servidor: int, id_emprestimo: int, id_coordenador: int) -> bool:
        sql = text("""
            DELETE FROM solicitacao
            WHERE id_servidor = :id_servidor
              AND id_emprestimo = :id_emprestimo
              AND id_coordenador = :id_coordenador
        """)

        params = {
            "id_servidor": id_servidor,
            "id_emprestimo": id_emprestimo,
            "id_coordenador": id_coordenador
        }
        try:
            result = db.execute(sql, params)
            db.commit()
            return result.rowcount > 0
        except Exception as e:
            db.rollback()
            print(f"Erro ao excluir solicitacao: {e}")
            return False