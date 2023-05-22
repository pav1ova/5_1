import requests
import time
from threading import Thread


def get_html(link):
    response = requests.get(link)
    print(link, len(response.text))

links = ['https://www.google.ru', 'https://yandex.ru', 'https://ya.ru', 'https://runinn.com', 'https://python-scripts.com', 'https://habr.com']

threads = [Thread(target=get_html, args=[links[i]]) for i in range(5)]

t_sequential = time.time()
for i in range(5):
    print(get_html(links[i]))
print(f'sequential using time: {time.time() - t_sequential}')

t_parallel = time.time()
for start in threads:
    start.start()
for j in threads:
    j.join()
print(f'parallel using time: {time.time() - t_parallel}')