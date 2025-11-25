class Coordenador:
    def __init__(self, matricula, nome, cpf, data_nascimento, id_escola):
        self.matricula = matricula
        self.nome = nome
        self.cpf = cpf
        self.data_nascimento = data_nascimento
        self.id_escola = id_escola
    
    def to_dict(self):
        return{
            "matricula": self.matricula,
            "nome": self.nome,
            "cpf": self.cpf,
            "data_nascimento": self.data_nascimento,
            "id_escola": self.id_escola
        }
    
    @classmethod
    def from_dict(cls, dicionario):
        return cls(
            matricula = dicionario.get("matricula"),
            nome = dicionario.get("nome"),
            cpf = dicionario.get("cpf"),
            data_nascimento = dicionario.get("data_nascimento"),
            id_escola = dicionario.get("id_escola")
        )
