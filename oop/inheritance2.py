from pprint import pprint


class Proteus:
    @staticmethod
    def move():
        print('движение')
    
    @staticmethod
    def eat():
        print('питание')
    
    @staticmethod
    def reproduce():
        print('размножение')


class Fish(Proteus):
    @staticmethod
    def breath():
        print('дыхание')


class Reptile(Fish):
    @staticmethod
    def hide():
        print('скрытность')


class Bird(Reptile):
    @staticmethod
    def fly():
        print('полёт')


class Mammal(Reptile):
    @staticmethod
    def care():
        print('забота')


class Human(Mammal):
    @staticmethod
    def speak():
        print('речь')


ivan = Human()
kesha = Bird()

# mro — method resolution order — порядок разрешения методов

# >>> pprint(ivan.__class__.__mro__)
# (<class '__main__.Human'>,
#  <class '__main__.Mammal'>,
#  <class '__main__.Reptile'>,
#  <class '__main__.Fish'>,
#  <class '__main__.Proteus'>,
#  <class 'object'>)
# >>>
# >>> pprint(kesha.__class__.__mro__)
# (<class '__main__.Bird'>,
#  <class '__main__.Reptile'>,
#  <class '__main__.Fish'>,
#  <class '__main__.Proteus'>,
#  <class 'object'>)

# >>> dir(ivan)
# ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'breath', 'care', 'eat', 'hide', 'move', 'reproduce', 'speak']
# >>>
# >>> dir(kesha)
# ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'breath', 'eat', 'fly', 'hide', 'move', 'reproduce']


# >>> pprint(object.__dict__, sort_dicts=False)
# mappingproxy({'__new__': <built-in method __new__ of type object at 0x00007FFFD4601570>,
#               '__repr__': <slot wrapper '__repr__' of 'object' objects>,
#               '__hash__': <slot wrapper '__hash__' of 'object' objects>,
#               '__str__': <slot wrapper '__str__' of 'object' objects>,
#               '__getattribute__': <slot wrapper '__getattribute__' of 'object' objects>,
#               '__setattr__': <slot wrapper '__setattr__' of 'object' objects>,
#               '__delattr__': <slot wrapper '__delattr__' of 'object' objects>,
#               '__lt__': <slot wrapper '__lt__' of 'object' objects>,
#               '__le__': <slot wrapper '__le__' of 'object' objects>,
#               '__eq__': <slot wrapper '__eq__' of 'object' objects>,
#               '__ne__': <slot wrapper '__ne__' of 'object' objects>,
#               '__gt__': <slot wrapper '__gt__' of 'object' objects>,
#               '__ge__': <slot wrapper '__ge__' of 'object' objects>,
#               '__init__': <slot wrapper '__init__' of 'object' objects>,
#               '__reduce_ex__': <method '__reduce_ex__' of 'object' objects>,
#               '__reduce__': <method '__reduce__' of 'object' objects>,
#               '__getstate__': <method '__getstate__' of 'object' objects>,
#               '__subclasshook__': <method '__subclasshook__' of 'object' objects>,
#               '__init_subclass__': <method '__init_subclass__' of 'object' objects>,
#               '__format__': <method '__format__' of 'object' objects>,
#               '__sizeof__': <method '__sizeof__' of 'object' objects>,
#               '__dir__': <method '__dir__' of 'object' objects>,
#               '__class__': <attribute '__class__' of 'object' objects>,
#               '__doc__': 'The base class of the class hierarchy.\n'
#                          '\n'
#                          'When called, it accepts no arguments and returns a '
#                          'new featureless\n'
#                          'instance that has no instance attributes and cannot '
#                          'be given any.\n'})

