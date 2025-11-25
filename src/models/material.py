from .equipamento import Equipamento

class Material(Equipamento):
    def __init__(self, id_equipamento, nome, descricao, localizacao, condicao, data_compra, status, categoria):

        super().__init__(id_equipamento, nome, descricao, localizacao, condicao, data_compra, status)
        
        self.categoria = categoria

    def to_dict(self):

        dicionario_base = super().to_dict()
        dicionario_base["categoria"] = self.categoria
        dicionario_base["tipo"] = "material"

        return dicionario_base
    
    @classmethod
    def from_dict(cls, dicionario):

        return cls(
            id_equipamento = dicionario.get("id_equipamento"),
            nome = dicionario.get("nome"),
            descricao = dicionario.get("descricao"),
            localizacao = dicionario.get("localizacao"),
            condicao = dicionario.get("condicao"),
            data_compra = dicionario.get("data_compra"),
            status = dicionario.get("status"),
            categoria = dicionario.get("categoria")
        )