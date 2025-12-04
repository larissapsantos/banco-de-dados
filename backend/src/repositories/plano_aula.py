from src.models.plano_aula import PlanoAula
from src.models.professor import Professor
from src.models.escola import Escola
from sqlalchemy.orm import Session

class PlanoAulaRepos:

    def criar(self, db: Session, planoAula: PlanoAula):
        db.add(planoAula)
        db.commit()
        db.refresh(planoAula)
        return planoAula

    def listar(self, db: Session):
        return db.query(PlanoAula).all()
    
    def buscar_por_id(self, db: Session, id: int):
        return db.query(PlanoAula).filter(PlanoAula.id == id).first()
    
    def listar_por_professor(self, db: Session, id_professor: int):
        return db.query(PlanoAula).filter(PlanoAula.id_professor == id_professor).all() # type: ignore
    
    def listar_por_escola(self, db: Session, id_escola: int):
        """
        Retorna planos + nome do professor para o Coordenador
        """
        # Busca (Plano, NomeProfessor) fazendo a junção das tabelas
        resultados = db.query(PlanoAula, Professor.nome).join(Professor).filter(
            Professor.id_escola == id_escola
        ).all()
        
        # Formata para um JSON bonito que o front entende
        lista_formatada = []
        for plano, nome_prof in resultados:
            item = plano.__dict__.copy() # Pega os dados do plano
            if '_sa_instance_state' in item: del item['_sa_instance_state'] # Limpeza técnica
            item['nome_professor'] = nome_prof # Adiciona o nome!
            lista_formatada.append(item)
            
        return lista_formatada

    def listar_pendentes_por_bairro(self, db: Session, bairro: str):
        """
        Retorna planos + nome do professor para o Admin
        """
        resultados = db.query(PlanoAula, Professor.nome).join(Professor).join(Escola).filter(
            Escola.bairro == bairro,
            PlanoAula.status == "ENVIADO" # type: ignore
        ).all()

        lista_formatada = []
        for plano, nome_prof in resultados:
            item = plano.__dict__.copy()
            if '_sa_instance_state' in item: del item['_sa_instance_state']
            item['nome_professor'] = nome_prof
            lista_formatada.append(item)
            
        return lista_formatada

    
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