class Calculadora:
    """
    @staticmethod:
    Indica que um método não requer acesso a instância ou à classe e funciona como uma função regular.
    """

    @staticmethod
    def somar(a, b):
        return a + b


resultado = Calculadora.somar(3, 4)
print(resultado)  # Saída: 7
