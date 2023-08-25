def decorator(funcao):
    def wrapper():
        print("Estou antes da execução da função passada como argumento")
        funcao()
        print("Estou depois da execução da função passada como argumento")

    return wrapper


def outra_funcao():
    print("Sou um belo argumento!")


if __name__ == '__main__':
    funcao_decorada = decorator(outra_funcao)
    funcao_decorada()
