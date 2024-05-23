class Liquid:
    def __init__(self, name: str, density: float):
        self.name = name
        self.density = density


# >>> pprint(Liquid.__dict__, sort_dicts=False)
# mappingproxy({'__module__': '__main__',
#               '__init__': <function Liquid.__init__ at 0x000002629205EFC0>,
#               '__dict__': <attribute '__dict__' of 'Liquid' objects>,
#               '__weakref__': <attribute '__weakref__' of 'Liquid' objects>,
#               '__doc__': None})
# >>> 
# >>> Liquid.__init__
# <function Liquid.__init__ at 0x000002629205EFC0>
# >>>
# >>> type(Liquid.__init__)
# <class 'function'>


# вызов объекта класса приводит к вызову специального метода метакласса, с помощью которого создаётся и конфигурируется экземпляр:
# def metaclass.__new__(cls, *args, **kwargs):
#     instance = __new__(cls)
#     cls.__init__(instance, *args, **kwargs)
#     return instance

breakpoint()

water = Liquid('вода', 1.00)
green_oil = Liquid('растительное масло', 0.94)

# >>> water.__dict__
# {'name': 'вода', 'density': 1.0}
# >>>
# >>> green_oil.__dict__
# {'name': 'растительное масло', 'density': 0.94}

water.viscosity = 1.789

# >>> water.__dict__
# {'name': 'вода', 'density': 1.0, 'viscosity': 1.789}
# >>>
# >>> green_oil.__dict__
# {'name': 'растительное масло', 'density': 0.94}

# >>> dir(green_oil)
# ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'density', 'name']
# >>>
# >>> dir(water)
# ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'density', 'name', 'viscosity']

