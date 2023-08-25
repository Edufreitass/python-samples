import requests
from concurrent.futures import ThreadPoolExecutor

urls = ['https://example.com/', 'https://httpbin.org/',
        'https://example.com/test_page']


def get_url(url):
    return requests.get(url)


with ThreadPoolExecutor(max_workers=3) as pool:
    print(list(pool.map(get_url, urls)))
    x = list(pool.map(get_url, urls))
    print('')
