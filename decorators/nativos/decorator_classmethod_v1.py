class Exemplo:
    """
    @classmethod:
    Usado para declarar métodos de classe, que recebem a classe como o primeiro argumento, em vez da instância.
    """
    contador = 0

    def __init__(self, nome):
        self.nome = nome
        Exemplo.contador += 1

    @classmethod
    def total_instancias(cls):
        return cls.contador


instancia1 = Exemplo("A")
instancia2 = Exemplo("B")

print(Exemplo.total_instancias())  # Saída: 2
