import requests, multiprocessing
from aws_lambda_powertools import Logger
from requests import HTTPError
import time

inicio = time.perf_counter()
logger = Logger()


def imprime():
    print('HELLO WORLD')
async def make_request():
    try:
        # response = requests.get(url='https://httpbin.org/status/500')
        req1 = await requests.get(url='https://24pullrequests.com/users.json')
        req2 = await requests.get(url='https://24pullrequests.com/users/andrew.json')
        print(f'1ªchamada: {req1.json()}')
        print(f'2ªchamada: {req2.json()}')
    except HTTPError as e:
        logger.exception(msg=e.response.text)
    except Exception as e:
        logger.exception(e)
    await imprime()


if __name__ == '__main__':
    make_request()
    # cod1 = multiprocessing.Process(target=make_request)
    # cod2 = multiprocessing.Process(target=make_request)
    #
    # cod1.start()
    # cod2.start()
    #
    # cod1.join()
    # cod2.join()

    fim = time.perf_counter()

    total = round(fim - inicio, 2)
    print(f'Tempo de execução: {total}')
