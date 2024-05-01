def fibonacci(elements: int = float('inf')) -> 'generator':
    n1, n2 = 1, 1
    if elements > 0:
        yield n1
    if elements > 1:
        yield n2
    cnt = 2
    while cnt < elements:
        n1, n2 = n2, n1 + n2
        yield n2
        cnt += 1


# >>> list(fibonacci(0))
# []
# >>> list(fibonacci(1))
# [1]
# >>> list(fibonacci(2))
# [1, 1]
# >>> list(fibonacci(3))
# [1, 1, 2]
# >>> list(fibonacci(5))
# [1, 1, 2, 3, 5]
# >>> list(fibonacci(12))
# [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144]

