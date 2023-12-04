from functools import wraps


def meu_decorator(func):
    """
    @functools.wraps:
    Mantém a assinatura e a documentação da função original ao criar um decorator.
    """

    @wraps(func)
    def wrapper(*args, **kwargs):
        print("Antes da chamada")
        resultado = func(*args, **kwargs)
        print("Depois da chamada")
        return resultado

    return wrapper


@meu_decorator
def minha_funcao():
    """Minha função."""
    print("Chamando a função")


minha_funcao()
print(minha_funcao.__name__)  # Saída: minha_funcao
print(minha_funcao.__doc__)  # Saída: Minha função.
