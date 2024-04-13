n1 = int(input('введите число: '))
sign = input('введите знак: ')
n2 = int(input('введите число: '))

if sign == '+':
    # print(f'n1 + n2 = {n1 + n2}')
    # то же самое
    print(f'{n1 + n2 = }')

elif sign == '-':
    print(f'{n1 - n2 = }')

elif sign == '*':
    print(f'{n1 * n2 = }')

elif sign == '/':
    if n2 != 0:
        print(f'{n1 / n2 = }')
    else:
        print('на ноль делить нельзя')

else:
    print('используйте символы + - * /')

