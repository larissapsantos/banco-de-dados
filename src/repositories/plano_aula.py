from src.models.plano_aula import PlanoAula
from sqlalchemy.orm import Session

class PlanoAulaRepos:

    def criar(self, db: Session, planoAula: PlanoAula):
        db.add(planoAula)
        db.commit()
        db.refresh(planoAula)
        return planoAula

    def listar(self, bd: Session):
        return bd.query(PlanoAula).all()
    
    def buscar_por_id(self, db: Session, id: int):
        return db.query(PlanoAula).filter(PlanoAula.id == id).first()
    
    def editar(self, db: Session, id: int, novos_dados: dict):
        plano_aula = self.buscar_por_id(db, id)
        if not plano_aula:
            return None
        campos_permitidos = ["titulo", "descricao", "status"]
        for campo in campos_permitidos:
            if campo in novos_dados:
                setattr(plano_aula, campo, novos_dados[campo])
        db.commit()
        db.refresh(plano_aula)
        return plano_aula
    
    def deletar(self, db: Session, id: int):
        plano_aula = self.buscar_por_id(db, id)
        if plano_aula:
            db.delete(plano_aula)
            db.commit()
        return plano_aula