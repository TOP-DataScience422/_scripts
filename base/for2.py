numbers = [10, 3, -2, 7, 16, 3]
numbers_len = len(numbers)
print(numbers, f'len={len(numbers)}\n')

for i in range(numbers_len):
    print(f'{i=}\t{numbers[i]=}')

# [10, 3, -2, 7, 16, 3] len=6

# i=0     numbers[i]=10
# i=1     numbers[i]=3
# i=2     numbers[i]=-2
# i=3     numbers[i]=7
# i=4     numbers[i]=16
# i=5     numbers[i]=3

# >>> i
# 5
# >>> numbers[6]
# IndexError: list index out of range

