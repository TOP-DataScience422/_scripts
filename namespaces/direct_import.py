# попытка импорта для файла 1.py приведёт к SyntaxError
# import 1

from importlib.util import spec_from_file_location, module_from_spec
from sys import path, modules

# путь к файлу
file_path = f'{path[0]}\\1.py'
# имя модуля
module_name = 'module_obj'

# создание вспомогательного объекта спецификации
spec_obj = spec_from_file_location(module_name, file_path)
# создание объекта модуля и идентификатора для него в текущем пространстве имён
module_obj = module_from_spec(spec_obj)

# внесение объекта модуля в системный словарь модулей
modules[module_name] = module_obj

# выполнение кода модуля
spec_obj.loader.exec_module(module_obj)


print(f'{module_obj.var = }')


# >>> module_obj
# <module 'module_obj' from '...\\scripts\\namespaces\\1.py'>
# >>>
# >>> modules['module_obj']
# <module 'module_obj' from '...\\scripts\\namespaces\\1.py'>

