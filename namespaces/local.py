# глобальная переменная — переменная во внутреннем пространстве имён текущего модуля
global_var = 'глобальная переменная'


def func1():
    local_var = 'локальная переменная'
    # global_var — обращение к глобальной переменной
    print(global_var, local_var)


def func2():
    local_var = 'локальная переменная'
    # global_var — создание локальной переменной
    global_var = 1000
    print('\nлокальное пространство имён вызова func2()', locals(), sep='\n')


def func3():
    global global_var
    local_var = 'локальная переменная'
    # global_var — изменение глобальной переменной
    global_var = 1000
    print('\nлокальное пространство имён вызова func3()', locals(), sep='\n')


func1()
print('\nтекущее пространство имён — модуля', locals(), sep='\n')
func2()
print('\nтекущее пространство имён — модуля', locals(), sep='\n')
func3()
print('\nтекущее пространство имён — модуля', locals(), sep='\n')

# приведёт к NameError
# print(global_var, local_var)

