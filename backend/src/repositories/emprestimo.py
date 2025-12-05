from src.models.emprestimo import Emprestimo
from sqlalchemy.orm import Session

class EmprestimoRepos:

    def criar(self, db: Session, emprestimo: Emprestimo):
        db.add(emprestimo)
        db.commit()
        db.refresh(emprestimo)
        return emprestimo

    def listar(self, db: Session):
        return db.query(Emprestimo).all()

    def buscar_por_id(self, db: Session, id: int):
        return db.query(Emprestimo).filter(Emprestimo.id == id).first()
    
    def editar(self, db: Session, id: int, novos_dados: dict):
        emprestimo = self.buscar_por_id(db, id)
        if not emprestimo:
            return None
        campos_permitidos = ["id_escola", "id_equipamento", "id_plano_aula"]
        for campo in campos_permitidos:
            if campo in novos_dados:
                setattr(emprestimo, campo, novos_dados[campo])
        db.commit()
        db.refresh(emprestimo)
        return emprestimo

    def deletar(self, db: Session, id: int):
        emprestimo = self.buscar_por_id(db, id)
        if emprestimo:
            db.delete(emprestimo)
            db.commit()
        return emprestimo
