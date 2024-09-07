from datetime import datetime as dt

print(f'{dt.now():%d %B (%a) %Y}')

from locale import setlocale, LC_ALL

setlocale(LC_ALL, 'ru-RU')

print(f'{dt.now():%d %B (%a) %Y}')
