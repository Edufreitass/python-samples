import concurrent.futures
import time

inicio = time.perf_counter()


def calcula_soma(numero):
    print('Iniciando a função...')
    soma = 0
    for i in range(numero):
        soma = soma + 1
    return 'Calculo finalizado'


if __name__ == '__main__':
    with concurrent.futures.ProcessPoolExecutor() as executor:
        cod1 = executor.submit(calcula_soma, 50_000_000)
        cod2 = executor.submit(calcula_soma, 50_000_000)

        print(cod1.result())
        print(cod2.result())

        fim = time.perf_counter()

        total = round(fim - inicio, 2)
        print(f'Tempo de execução: {total}')
