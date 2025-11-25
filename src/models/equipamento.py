class Equipamento:
    def __init__(self, id_equipamento, nome, descricao, localizacao, condicao, data_compra, status):
        self.id_equipamento = id_equipamento
        self.nome = nome
        self.descricao = descricao
        self.localizacao = localizacao
        self.condicao = condicao
        self.data_compra = data_compra
        self.status = status
    
    def to_dict(self):
        return {
            "id_equipamento": self.id_equipamento,
            "nome": self.nome,
            "descricao": self.descricao,
            "localizacao": self.localizacao,
            "condicao": self.condicao,
            "data_compra": self.data_compra,
            "status": self.status
        }

    @classmethod
    def from_dict(cls, dicionario):
        return cls(
            id_equipamento = dicionario.get("id_equipamento"),
            nome = dicionario.get("nome"),
            descricao = dicionario.get("descricao"),
            localizacao = dicionario.get("localizacao"),
            condicao = dicionario.get("condicao"),
            data_compra = dicionario.get("data_compra"),
            status = dicionario.get("status")
        )