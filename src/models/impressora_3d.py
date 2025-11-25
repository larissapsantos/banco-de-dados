from .equipamento import Equipamento

class Impressora3D(Equipamento):
    def __init__(self, id_equipamento, nome, descricao, localizacao, condicao, data_compra, status, manual):

        super().__init__(id_equipamento, nome, descricao, localizacao, condicao, data_compra, status)
        
        self.manual = manual

    def to_dict(self):

        dicionario_base = super().to_dict()
        dicionario_base["manual"] = self.manual
        dicionario_base["tipo"] = "impressora_3d"

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
            manual = dicionario.get("manual")
        )
