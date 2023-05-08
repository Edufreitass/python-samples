import concurrent.futures
import time

inicio = time.perf_counter()


def calcula_soma(numero):
    print('Iniciando a função...')
    soma = 0
    for i in range(numero):
        soma = soma + 1
    return f'Calculo finalizado - num: {numero}'


if __name__ == '__main__':
    with concurrent.futures.ProcessPoolExecutor() as executor:
        nums = [10_000_000, 30_000_000, 50_000_000]
        cods = executor.map(calcula_soma, nums)

        for cod in cods:
            print(cod)

        fim = time.perf_counter()

        total = round(fim - inicio, 2)
        print(f'Tempo de execução: {total}')
