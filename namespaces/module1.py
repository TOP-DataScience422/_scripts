"""
Точка входа.
"""
print('начало выполнения модуля точки входа')

import module2

print({k: v for k, v in globals().items() if not k.startswith('_')})

print('конец выполнения модуля точки входа')


# начало выполнения модуля точки входа
# начало выполнения модуля 2
# начало выполнения модуля 3
# {'rounder': <function rounder at 0x000001F58236F1A0>}
# конец выполнения модуля 3
# {'rounder': <function rounder at 0x000001F58236F1A0>, 'pi': 3.141592}
# конец выполнения модуля 2
# {'module2': <module 'module2' from '...\\scripts\\namespaces\\module2.py'>}
# конец выполнения модуля точки входа

# >>> import module3
# >>>
# >>> {k: v for k, v in globals().items() if not k.startswith('_')}
# {'module2': <module 'module2' from '...\\scripts\\namespaces\\module2.py'>, 'module3': <module 'module3' from '...\\scripts\\namespaces\\module3.py'>}
# >>>
# >>> module2.pi
# 3.141592
# >>>
# >>> module2.rounder
# <function rounder at 0x000001F58236F1A0>
# >>>
# >>> module3.rounder
# <function rounder at 0x000001F58236F1A0>
# >>>
# >>> module2.rounder is module3.rounder
# True

