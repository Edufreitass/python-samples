class Configuracao:
    """
    @classmethod + @property:
    Usado para criar propriedades de classe
    """
    _limite = 100

    @classmethod
    @property
    def limite(cls):
        return cls._limite


print(Configuracao.limite)  # Saída: 100
