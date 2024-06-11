class Person:
    def __init__(self, last_name, first_name, patr_name):
        self.last = last_name
        self.first = first_name
        self.patr = patr_name
    
    def __repr__(self):
        return f'{self.first[0]}. {self.patr[0]}. {self.last}'


class Student(Person):
    # допустимый вариант
    # def __init__(self, last_name, first_name, patr_name, year):
    # идеальный вариант
    def __init__(self, last_name, first_name, patr_name, year=1):
        # Person.__init__(self, last_name, first_name, patr_name)
        # аналогичный вызов
        # self.__class__.__mro__[1].__init__(self, last_name, first_name, patr_name)
        # аналогичный вызов
        super().__init__(last_name, first_name, patr_name)
        self.year = year
    
    def __repr__(self):
        return f'{super().__repr__()}, {self.year} курс'


teacher = Person('Коробейников', 'Игорь', 'Дмитриевич')
# breakpoint()
stud1 = Student('Долгохватов', 'Николай', 'Александрович')
stud2 = Student('Школяров', 'Артём', 'Георгиевич', 4)

# >>> teacher
# И. Д. Коробейников
# >>>
# >>> stud1
# Н. А. Долгохватов, 1 курс
# >>>
# >>> stud2
# А. Г. Школяров, 4 курс

