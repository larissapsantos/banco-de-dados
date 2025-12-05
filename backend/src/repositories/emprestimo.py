from sqlalchemy.orm import Session
from sqlalchemy import text
from typing import List, Dict, Optional

class EmprestimoRepos:
    def criar(self, db: Session, emprestimo: dict) -> Optional[Dict]:
        sql = text("""
            INSERT INTO emprestimo (id_escola, id_equipamento, id_plano_aula, data_hora)
            VALUES (:id_escola, :id_equipamento, :id_plano_aula, NOW())
        """)
        try:
            result = db.execute(sql, emprestimo)
            id = int(result.lastrowid)
            sql_select = text("""
                SELECT id, data_hora, id_escola, id_equipamento, id_plano_aula FROM emprestimo WHERE id = :id
            """)
            result = db.execute(sql_select, {"id": id}).mappings().first()
            db.commit()
            return result
        except Exception as e:
            db.rollback()
            print(f"Erro ao criar empréstimo: {e}")
            return None

    def listar(self, db: Session) -> List[Dict]:
        sql = text("SELECT * FROM emprestimo ORDER BY id")
        result = db.execute(sql).mappings().all()
        return result

    def buscar_por_id(self, db: Session, id: int) -> Optional[Dict]:
        sql = text("""
            SELECT * FROM emprestimo
            WHERE id = :id
            LIMIT 1
        """)
        result = db.execute(sql, {"id": id}).mappings().first()
        return result
    
    def editar(self, db: Session, id: int, novos_dados: dict) -> Optional[Dict]:
        campos_permitidos = ["id_equipamento", "id_plano_aula"]
        atualizacoes = {}
        
        for campo in campos_permitidos:
            if campo in novos_dados:
                atualizacoes[campo] = novos_dados[campo]

        if not atualizacoes:
            return self.buscar_por_id(db, id)

        atualizacoes['id'] = id
        campos_para_atualizar = ", ".join([f"{campo} = :{campo}" for campo in atualizacoes if campo != 'id'])
        
        sql = text(f"""
            UPDATE emprestimo
            SET {campos_para_atualizar}
            WHERE id = :id
        """)
        try:
            db.execute(sql, atualizacoes)
            sql_select = text("""
                SELECT * FROM emprestimo WHERE id = :id
            """)
            result = db.execute(sql_select, {"id": id}).mappings().first()
            db.commit()
            return result
        except Exception as e:
            db.rollback()
            print(f"Erro ao editar empréstimo {id}: {e}")
            return None
    
    def excluir(self, db: Session, id: int) -> bool:
        sql = text("""
            DELETE FROM emprestimo
            WHERE id = :id
        """)
        try:
            result = db.execute(sql, {"id": id})
            db.commit()
            return result.rowcount > 0
        except Exception as e:
            db.rollback()
            print(f"Erro ao excluir empréstimo {id}: {e}")
            return False