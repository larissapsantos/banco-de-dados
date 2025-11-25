class Administrador:
    def __init__(self, matricula, nome, cargo, cpf, email):
        self.matricula = matricula
        self.nome = nome
        self.cargo = cargo
        self.cpf = cpf
        self.email = email
    
    def to_dict(self):
        return {
            "matricula": self.matricula,
            "nome": self.nome,
            "cargo": self.cargo,
            "cpf": self.cpf,
            "email": self.email
        }

    @classmethod
    def from_dict(cls, dicionario):
        return cls(
            matricula = dicionario.get("matricula"),
            nome = dicionario.get("nome"),
            cargo = dicionario.get("cargo"),
            cpf = dicionario.get("cpf"),
            email = dicionario.get("email")
        )