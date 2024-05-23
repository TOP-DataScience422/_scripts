from pprint import pprint


class Fruit:
    name: str
    color: str
    weight: float


# >>> Fruit
# <class '__main__.Fruit'>
# >>>
# >>> pprint(Fruit.__dict__, sort_dicts=False)
# mappingproxy({'__module__': '__main__',
#               '__annotations__': {'name': <class 'str'>,
#                                   'color': <class 'str'>,
#                                   'weight': <class 'float'>},
#               '__dict__': <attribute '__dict__' of 'Fruit' objects>,
#               '__weakref__': <attribute '__weakref__' of 'Fruit' objects>,
#               '__doc__': None})

Fruit.attr = 'атрибут класса'

# >>> pprint(Fruit.__dict__, sort_dicts=False)
# mappingproxy({'__module__': '__main__',
#               '__annotations__': {'name': <class 'str'>,
#                                   'color': <class 'str'>,
#                                   'weight': <class 'float'>},
#               '__dict__': <attribute '__dict__' of 'Fruit' objects>,
#               '__weakref__': <attribute '__weakref__' of 'Fruit' objects>,
#               '__doc__': None,
#               'attr': 'атрибут класса'})
# >>>
# >>> Fruit.attr
# 'атрибут класса'

apple = Fruit()

# >>> apple
# <__main__.Fruit object at 0x0000020C2FA16A50>
# >>>
# >>> apple.__dict__
# {}

apple.name = 'яблоко'
apple.color = 'зелёное'
apple.weight = 0.150

# >>> apple.__dict__
# {'name': 'яблоко', 'color': 'зелёное', 'weight': 0.15}

peach = Fruit()

peach.name = 'персик'
peach.color = 'оранжевый'
peach.weight = 0.120

# >>> peach
# <__main__.Fruit object at 0x0000020C2FA16AE0>
# >>>
# >>> peach.__dict__
# {'name': 'персик', 'color': 'оранжевый', 'weight': 0.12}

# >>> apple.name
# 'яблоко'
# >>> peach.name
# 'персик'

fruits = [apple, peach]
for fruit in fruits:
    print(f'{fruit.color} {fruit.name} весит {fruit.weight} кг')

# зелёное яблоко весит 0.15 кг
# оранжевый персик весит 0.12 кг

pear = Fruit()

pear.n = 'груша'
pear.colorized = 'зеленовато-жёлтая'
pear.ripe = 90

# >>> pear.__dict__
# {'n': 'груша', 'colorized': 'зеленовато-жёлтая', 'ripe': 90}

fruits.append(pear)
for fruit in fruits:
    print(f'{fruit.color} {fruit.name} весит {fruit.weight} кг')

# зелёное яблоко весит 0.15 кг
# оранжевый персик весит 0.12 кг
# AttributeError: 'Fruit' object has no attribute 'color'


# >>> apple.__class__
# <class '__main__.Fruit'>
# >>>
# >>> peach.__class__
# <class '__main__.Fruit'>
# >>>
# >>> pear.__class__
# <class '__main__.Fruit'>
# >>>
# >>> Fruit is apple.__class__ is peach.__class__ is pear.__class__
# True


# >>> apple.attr
# 'атрибут класса'
# >>>
# >>> peach.attr
# 'атрибут класса'
# >>>
# >>> pear.attr
# 'атрибут класса'

pear.attr = 'атрибут экземпляра'

# >>> pear.__dict__
# {'n': 'груша', 'colorized': 'зеленовато-жёлтая', 'ripe': 90, 'attr': 'атрибут экземпляра'}
# >>>
# >>> pprint(Fruit.__dict__, sort_dicts=False)
# mappingproxy({'__module__': '__main__',
#               '__annotations__': {'name': <class 'str'>,
#                                   'color': <class 'str'>,
#                                   'weight': <class 'float'>},
#               '__dict__': <attribute '__dict__' of 'Fruit' objects>,
#               '__weakref__': <attribute '__weakref__' of 'Fruit' objects>,
#               '__doc__': None,
#               'attr': 'атрибут класса'})
# >>>
# >>> pear.attr
# 'атрибут экземпляра'

