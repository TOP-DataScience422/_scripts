# внешние пакеты
...
# стандартная библиотека
from datetime import datetime as dt
# текущий проект
import reading as paths

# >>> paths.__name__
# 'reading'


lines = [
    'новая третья строчка\n',
    'новая четвёртая строчка\n',
]
with open(paths.data_path, 'w', encoding='utf-8') as fileout:
    fileout.write('новая первая строчка\nновая вторая строчка')
    fileout.writelines(lines)
    print('новая пятая строчка', file=fileout)


# предварительно готовим данные для записи
new_entry = f'{dt.now():%Y/%m/%d - %H:%M:%S}'
# затем осуществляем запись
with open(paths.log_path, 'w', encoding='utf-8') as fileout:
    print(new_entry, file=fileout)

