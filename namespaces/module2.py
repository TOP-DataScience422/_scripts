"""
Вспомогательный модуль 1: данные.
"""
print('начало выполнения модуля 2')

from module3 import rounder

pi = 3.141592

print({k: v for k, v in globals().items() if not k.startswith('_')})

print('конец выполнения модуля 2')
