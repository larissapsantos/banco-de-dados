class Solicitacao:
    def __init__(self, id_servidor, id_emprestimo, id_coordenador):
        self.id_servidor = id_servidor
        self.id_emprestimo = id_emprestimo
        self.id_coordenador = id_coordenador

    def to_dict(self):
        return {
            "id_servidor": self.id_servidor,
            "id_emprestimo": self.id_emprestimo,
            "id_coordenador": self.id_coordenador
        }

    @classmethod
    def from_dict(cls, dicionario):
        return cls(
            id_servidor = dicionario.get("id_servidor"),
            id_emprestimo = dicionario.get("id_emprestimo"),
            id_coordenador = dicionario.get("id_coordenador")
        )