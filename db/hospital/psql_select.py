# внешние пакеты
from psycopg import connect
# стандартная библиотека
from json import loads as json_loads
from pprint import pprint
from pathlib import Path
from sys import path
# текущий проект
import queries


config_path = Path(path[0]) / 'config_psql.json'
config = json_loads(config_path.read_text())

connection = connect(**config)

with connection.cursor() as cursor:
    cursor.execute(queries.sel_doctors_avg_salary)
    doctors_avg_salary = cursor.fetchall()


# >>> doctors_avg_salary
# [(Decimal('56800'),)]

