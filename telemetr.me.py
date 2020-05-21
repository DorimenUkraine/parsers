from time import sleep
import requests
from bs4 import BeautifulSoup

# Не уверен, что все знакомы с библиотекой fake_useragent.
# Довольно удобна для парсинга, создает фейк user-agent'a.
from fake_useragent import UserAgent, FakeUserAgentError

try:
    ua = UserAgent()
except FakeUserAgentError:
    pass

# создаем заголовок
headers = {'User-Agent': ua.random}

url = 'https://telemetr.me/channels/'

with requests.Session() as se:
    se.headers = headers


resp = se.get(url)

index = BeautifulSoup(resp.content, 'html.parser')

max_page = int(input('Введите предполагаемое количество страниц: '))

pages = []

input_category = input('Введите категорию (учитывая регистр как на сайте): ')

for x in range(1, max_page + 1):
    sleep(3)
    sort = pages.append(se.get(f'https://telemetr.me/channels/cat/{input_category}/?page=' + str(x)))

for sort in pages:
    pars = BeautifulSoup(sort.content, 'html.parser')

    for el in pars.select('.wd-300'):
        link = el.find('a')
        try:
            print(link.get('href'))
            with open(f'{input_category}.txt', 'a') as file:
                file.write(f'{link.get("href")}\n')

        except AttributeError as error:
            print(f'Произошла ошибка {error}. Работа скрипта продолжается.')
            continue




