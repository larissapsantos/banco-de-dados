from src.models.solicitacao import Solicitacao
from sqlalchemy.orm import Session

class SolicitacaoRepositorio:

    def criar(self, db: Session, solicitacao: Solicitacao):
        db.add(solicitacao)
        db.commit()
        db.refresh(solicitacao)
        return solicitacao

    def listar(self, db: Session):
        return db.query(Solicitacao).all()

    def buscar_por_chave_composta(self, db: Session, id_administrador: int, id_emprestimo: int, id_coordenador: int):
        return db.query(Solicitacao).filter(
            Solicitacao.id_administrador == id_administrador,
            Solicitacao.id_emprestimo == id_emprestimo,
            Solicitacao.id_coordenador == id_coordenador
        ).first()

    def editar(self, db: Session, id_administrador: int, id_emprestimo: int, id_coordenador: int, novos_dados: dict):
        solicitacao = self.buscar_por_chave_composta(
            db, id_administrador, id_emprestimo, id_coordenador
        )
        if solicitacao is None:
            return None
        campos_permitidos = ["status"]
        for campo in campos_permitidos:
            if campo in novos_dados:
                setattr(solicitacao, campo, novos_dados[campo])
        db.commit()
        db.refresh(solicitacao)
        return solicitacao

    def deletar(self, db: Session, id_administrador: int, id_emprestimo: int, id_coordenador: int):
        solicitacao = self.buscar_por_chave_composta(
            db, id_administrador, id_emprestimo, id_coordenador
        )
        if solicitacao:
            db.delete(solicitacao)
            db.commit()
        return solicitacao