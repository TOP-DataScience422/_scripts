def mean(num1: float, num2: float, *numbers: float, digits: int = 2) -> float:
    print(f'\n{num1=}\t{num2=}\n{type(numbers)}\t{numbers=}')
    numbers = (num1, num2, *numbers)
    return round(sum(numbers) / len(numbers), digits)


mean(2, 3)

# num1=2  num2=3
# <class 'tuple'> numbers=()


mean(2, 3, 4, 5)

# num1=2  num2=3
# <class 'tuple'> numbers=(4, 5)


mean(*range(10, 30, 2))

# num1=10 num2=12
# <class 'tuple'> numbers=(14, 16, 18, 20, 22, 24, 26, 28)


mean(10, 20, 18, 12, digits=0)

# num1=10 num2=20
# <class 'tuple'> numbers=(18, 12)

