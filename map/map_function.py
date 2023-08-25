import concurrent.futures
import time

inicio = time.perf_counter()
def sem_map():
    # numbers = [1, 2, 3, 4, 5]
    lst = list(range(1, 1_000_000_000))
    numbers = lst
    squared = []

    for num in numbers:
        squared.append(num ** 2)

    # print(squared)
    fim = time.perf_counter()

    total = round(fim - inicio, 2)
    print(f'Tempo de execução sem map: {total}')


def com_map():
    def square(number):
        return number ** 2

    # numbers = [1, 2, 3, 4, 5]
    lst = list(range(1, 1_000_000_000))
    numbers = lst
    squared = map(square, numbers)

    # print(list(squared))
    fim = time.perf_counter()

    total = round(fim - inicio, 2)
    print(f'Tempo de execução com map: {total}')


if __name__ == '__main__':
    sem_map()
    com_map()
