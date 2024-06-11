from pprint import pprint


# родительский (parent), базовый (base), предок, надкласс (superclass)
class Parent:
    attr1 = 'атрибут базового класса'
    
    def __init__(self, val):
        self.inst_attr1 = val
    
    @staticmethod
    def super_method():
        print('вызов метода базового класса')


# дочерний (child), производный (inherent), потомок, подкласс (subclass)
class Child(Parent):
    attr2 = 'атрибут производного класса'
    
    def __init__(self, val):
        self.inst_attr2 = val
    
    @staticmethod
    def sub_method():
        print('вызов метода производного класса')


p1 = Parent(222)
c1 = Child(333)

# >>> pprint(Parent.__dict__, sort_dicts=False)
# mappingproxy({'__module__': '__main__',
#               'attr1': 'атрибут базового класса',
#               '__init__': <function Parent.__init__ at 0x0000029110C9EFC0>,
#               'super_method': <staticmethod(<function Parent.super_method at 0x0000029110CE76A0>)>,
#               '__dict__': <attribute '__dict__' of 'Parent' objects>,
#               '__weakref__': <attribute '__weakref__' of 'Parent' objects>,
#               '__doc__': None})
# >>>
# >>> p1.__dict__
# {'inst_attr1': 222}

# >>> pprint(Child.__dict__, sort_dicts=False)
# mappingproxy({'__module__': '__main__',
#               'attr2': 'атрибут производного класса',
#               '__init__': <function Child.__init__ at 0x0000029110CE7740>,
#               'sub_method': <staticmethod(<function Child.sub_method at 0x0000029110CE77E0>)>,
#               '__doc__': None})
# >>>
# >>> c1.__dict__
# {'inst_attr2': 333}

# >>> c1.inst_attr2
# 333
# >>> c1.attr2
# 'атрибут производного класса'
# >>>
# >>> c1.attr1
# 'атрибут базового класса'

# >>> c1.sub_method
# <function Child.sub_method at 0x0000029110CE77E0>
# >>>
# >>> c1.sub_method()
# вызов метода производного класса
# >>>
# >>> c1.super_method
# <function Parent.super_method at 0x0000029110CE76A0>
# >>>
# >>> c1.super_method()
# вызов метода базового класса


class Child2(Parent):
    pass


c2 = Child2(444)

# >>> Child2.__init__
# <function Parent.__init__ at 0x0000029110C9EFC0>
# >>>
# >>> c2.__dict__
# {'inst_attr1': 444}

