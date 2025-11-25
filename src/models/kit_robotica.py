from .equipamento import Equipamento

class KitRobotica(Equipamento):
    def __init__(self, id_equipamento, nome, descricao, localizacao, condicao, data_compra, status, fabricante):

        super().__init__(id_equipamento, nome, descricao, localizacao, condicao, data_compra, status)

        self.fabricante = fabricante

    def to_dict(self):

        # pegamos o dicionario da classe pai (equipamento)
        dicionario_base = super().to_dict()

        # adicionamos o atributo específico de KitRobotica (fabricante) no dicionario da classe pai
        dicionario_base["fabricante"] = self.fabricante

        # adicionamos um tipo para ajudar a identificar que é o kit
        dicionario_base["tipo"] = "kit_robotica"

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
            fabricante = dicionario.get("fabricante")
        )