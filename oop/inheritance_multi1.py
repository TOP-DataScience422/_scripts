class A:
    attr = 'атрибут класса A'


class B:
    attr = 'атрибут класса B'


class C(A, B):
    pass


class D(B, A):
    pass


# >>> C.attr
# 'атрибут класса A'
# >>>
# >>> D.attr
# 'атрибут класса B'

# >>> C.__mro__
# (<class '__main__.C'>, <class '__main__.A'>, <class '__main__.B'>, <class 'object'>)
# >>>
# >>> D.__mro__
# (<class '__main__.D'>, <class '__main__.B'>, <class '__main__.A'>, <class 'object'>)

