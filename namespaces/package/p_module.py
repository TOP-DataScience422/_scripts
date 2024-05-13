"""
Точка входа пакета.
"""

import package.subpackage

print({k: v for k, v in package.subpackage.__dict__.items() if not k.startswith('_')})

# {'sp_module': <module 'subpackage.sp_module' from '...\\package\\subpackage\\sp_module.py'>, 'var1': 100, 'var3': 0.98, 'var5': [10, -10, 3]}


# >>> subpackage
# <module 'subpackage' from '...\\package\\subpackage\\__init__.py'>


# >>> subpackage.var1
# 100
# >>> subpackage.var2
# AttributeError: module 'subpackage' has no attribute 'var2'. Did you mean: 'var1'?
# >>>
# >>> subpackage.var3
# 0.98
# >>>
# >>> subpackage.sp_module.var1
# 100
# >>> subpackage.sp_module.var2
# 'слово'
# >>> subpackage.sp_module.var3
# 0.98


# >>> subpackage.sp_module.__package__
# 'subpackage'

