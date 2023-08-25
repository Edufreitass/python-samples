# "Criador" de funções de potência
def cria_potencia(x):
    def potencia(num):
        return x ** num

    return potencia


if __name__ == '__main__':
    # Potência de 2 e 3
    potencia_2 = cria_potencia(2)
    potencia_3 = cria_potencia(3)

    # Resultado
    print(potencia_2(2))  # 2 ** 2 = 4
    print(potencia_3(2))  # 3 ** 2 = 9
