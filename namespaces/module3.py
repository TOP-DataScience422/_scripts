"""
Вспомогательный модуль 2: функции.
"""
print('начало выполнения модуля 3')

def rounder(number: float) -> int:
    return round(number)

print({k: v for k, v in globals().items() if not k.startswith('_')})

print('конец выполнения модуля 3')
