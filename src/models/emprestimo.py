class Emprestimo:
    def __init__(self, id_emprestimo, quantidade, horario, data, id_escola, id_equipamento, id_plano_aula):
        self.id_emprestimo = id_emprestimo
        self.quantidade = quantidade
        self.horario = horario
        self.data = data
        self.id_escola = id_escola
        self.id_equipamento = id_equipamento
        self.id_plano_aula = id_plano_aula

    def to_dict(self):
        return {
            "id_emprestimo": self.id_emprestimo,
            "quantidade": self.quantidade,
            "horario": self.horario,
            "data": self.data,
            "id_escola": self.id_escola,
            "id_equipamento": self.id_equipamento,
            "id_plano_aula": self.id_plano_aula
        }

    @classmethod
    def from_dict(cls, dicionario):
        return cls(
            id_emprestimo = dicionario.get("id_emprestimo"),
            quantidade = dicionario.get("quantidade"),
            horario = dicionario.get("horario"),
            data = dicionario.get("data"),
            id_escola = dicionario.get("id_escola"),
            id_equipamento = dicionario.get("id_equipamento"),
            id_plano_aula = dicionario.get("id_plano_aula")
        )