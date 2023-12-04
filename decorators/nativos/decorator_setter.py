class Pessoa:
    """
    @setter:
    Define o método setter para uma propriedade.
    """

    def __init__(self, nome):
        self._nome = nome

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome


p = Pessoa("Maria")
p.nome = "Joana"
print(p.nome)  # Saída: Joana
