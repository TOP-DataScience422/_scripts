# 1, 1, 2, 2, 3, 3, 4, 4, 5, 5


def seq_doubler(start: int, end: int, step: int = 1) -> 'generator':
    for n in range(start, end, step):
        yield n
        yield n


# >>> list(seq_doubler(1, 6))
# [1, 1, 2, 2, 3, 3, 4, 4, 5, 5]

