import multiprocessing
import time

inicio = time.perf_counter()


def calcula_soma():
    print('Iniciando a função...')
    soma = 0
    for i in range(50_000_000):
        soma = soma + 1
    print('Calculo finalizado')


if __name__ == '__main__':
    cod1 = multiprocessing.Process(target=calcula_soma)
    cod2 = multiprocessing.Process(target=calcula_soma)

    cod1.start()
    cod2.start()

    cod1.join()
    cod2.join()

    fim = time.perf_counter()

    total = round(fim - inicio, 2)
    print(f'Tempo de execução: {total}')
