data1 = [
    (1, 2, 3),
    (4, 5, 6),
]
data2 = [
    [
        (1, 2, 3),
        (4, 5, 6),
    ],
    [
        (7, 8, 9),
        (10, 11, 12),
    ],
]
data3 = [
    (
        [
            {1, 2, 3},
            {4, 5, 6},
        ],
        [
            {7, 8, 9},
            {10, 11, 12},
        ],
    ),
    (
        [
            {13, 14, 15},
            {16, 17, 18},
        ],
        [
            {19, 20, 21},
            {22, 23, 24},
        ],
    ),
]

def flatten(data: 'iterable') -> list[int]:
    result = []
    for elem in data:
        if isinstance(elem, (tuple, list, set)):
            result.extend(flatten(elem))
        else:
            result.append(elem)
    return result


# >>> flatten([1, 2, 3])
# [1, 2, 3]

# >>> flatten(data1)
# [1, 2, 3, 4, 5, 6]

# >>> flatten(data2)
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

# >>> flatten(data3)
# [1, 2, 3, 4, 5, 6, 8, 9, 7, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 24, 22, 23]

