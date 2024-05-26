from pprint import pprint


class PrintingObject:
    def __init__(self, text: str):
        self.text = text
    
    def print_lines(self, number_of_lines: int = 1):
        # breakpoint()
        lines = self.text.split('\n', number_of_lines)[:number_of_lines]
        print('\n'.join(lines))
    
    def print_page(self):
        page = self.text.split('\f', 1)[0]
        print(page)


# >>> PrintingObject.__init__
# <function PrintingObject.__init__ at 0x000001661CB3EFC0>
# >>>
# >>> PrintingObject.print_lines
# <function PrintingObject.print_lines at 0x000001661CB3F060>
# >>>
# >>> PrintingObject.print_page
# <function PrintingObject.print_page at 0x000001661CB3F100>

# >>> PrintingObject.print_lines()
# TypeError: PrintingObject.print_lines() missing 1 required positional argument: 'self'

po1 = PrintingObject('''Commands that the debugger doesn’t recognize are assumed to be Python statements and are executed in the context of the program being debugged. Python statements can also be prefixed with an exclamation point (!).
This is a powerful way to inspect the program being debugged; it is even possible to change a variable or call a function. When an exception occurs in such a statement, the exception name is printed but the debugger’s state is not changed.''')

# >>> po1.__init__
# <bound method PrintingObject.__init__ of <__main__.PrintingObject object at 0x000001661CB36AB0>>
# >>>
# >>> po1.print_lines
# <bound method PrintingObject.print_lines of <__main__.PrintingObject object at 0x000001661CB36AB0>>
# >>>
# >>> po1.print_page
# <bound method PrintingObject.print_page of <__main__.PrintingObject object at 0x000001661CB36AB0>>

# при обращении к функции во внутреннем пространстве имён класса от экземпляра этого класса происходит подмена объекта функции объектом метода, при вызове которого осуществялется подмена вызова:
# po1.print_lines() --> PrintingObject.print_lines(po1)

# >>> po1.print_lines()
# Commands that the debugger doesn’t recognize are assumed to be Python statements and are executed in the context of the program being debugged. Python statements can also be prefixed with an exclamation point (!).

# >>> PrintingObject.print_lines(po1)
# Commands that the debugger doesn’t recognize are assumed to be Python statements and are executed in the context of the program being debugged. Python statements can also be prefixed with an exclamation point (!).

# >>> po1.print_page()
# Commands that the debugger doesn’t recognize are assumed to be Python statements and are executed in the context of the program being debugged. Python statements can also be prefixed with an exclamation point (!).
# This is a powerful way to inspect the program being debugged; it is even possible to change a variable or call a function. When an exception occurs in such a statement, the exception name is printed but the debugger’s state is not changed.
# >>>
# >>> PrintingObject.print_page(po1)
# Commands that the debugger doesn’t recognize are assumed to be Python statements and are executed in the context of the program being debugged. Python statements can also be prefixed with an exclamation point (!).
# This is a powerful way to inspect the program being debugged; it is even possible to change a variable or call a function. When an exception occurs in such a statement, the exception name is printed but the debugger’s state is not changed.


# в отладчике:
# >>> po1.print_lines()
# 
# > methods1.py(10) print_lines()
#   -> lines = self.text.split('\n', number_of_lines)[:number_of_lines]
# 
# (Pdb) args
# self = <__main__.PrintingObject object at 0x000001BFE89272F0>
# number_of_lines = 1
# 
# (Pdb) self is po1
# True


# общий вид работы связанного метода:
# instance.method(*args, **kwargs) --> instance.__class__.method(instance, *args, **kwargs)

