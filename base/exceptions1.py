# data = input('введите число: ')
# if data.isdigit():
#     n = int(data)
#     print(n ** 2)
# else:
#     print('используйте только цифры')


try:
    n = int(input('введите число: '))
except ValueError:
    print('используйте только цифры')
else:
    print(n**2)


# число: 12
# 144

# число: 1 2
# используйте только цифры

