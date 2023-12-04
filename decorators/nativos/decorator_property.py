class Pessoa:
    """
    @property:
    Transforma um método em uma propriedade somente de leitura.
    """

    def __init__(self, nome):
        self._nome = nome

    @property
    def nome(self):
        return self._nome


p = Pessoa("João")
print(p.nome)  # Saída: João
