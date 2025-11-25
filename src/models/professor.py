class Professor:
    def __init__(self, matricula, nome, situacao, data_admissao, id_escola):
        self.matricula = matricula
        self.nome = nome
        self.situacao = situacao
        self.data_admissao = data_admissao
        self.id_escola = id_escola
    
    def to_dict(self):
        return{
            "matricula": self.matricula,
            "nome": self.nome,
            "situacao": self.situacao,
            "data_admissao": self.data_admissao,
            "id_escola": self.id_escola
        }
    
    @classmethod
    def from_dict(cls, dicionario):
        return cls(
            matricula = dicionario.get("matricula"),
            nome = dicionario.get("nome"),
            situacao = dicionario.get("situacao"),
            data_admissao = dicionario.get("data_admissao"),
            id_escola = dicionario.get("id_escola")
        )