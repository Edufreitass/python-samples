class Pessoa:
    """
    @property + @setter + @deleter:
    Cria propriedades com métodos getter, setter e deleter.
    """

    def __init__(self, nome):
        self._nome = nome

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome

    @nome.deleter
    def nome(self):
        del self._nome


p = Pessoa("Maria")
del p.nome
# Agora a instância não possui o atributo nome
