from pandas import Series


numbers = [3, -1, 6, 5, 0, -7, 1]
row_lbls = [f'val_{i}' for i in range(1, len(ns)+1)]

# >>> ns1 = Series(numbers, index=row_lbls)
# >>> ns1
# val_1    3
# val_2   -1
# val_3    6
# val_4    5
# val_5    0
# val_6   -7
# val_7    1
# dtype: int64
# >>>
# >>> ns1.index
# Index(['val_1', 'val_2', 'val_3', 'val_4', 'val_5', 'val_6', 'val_7'], dtype='object')

labels_numbers = dict(zip(row_lbls, numbers))

# >>> labels_numbers
# {'val_1': 3, 'val_2': -1, 'val_3': 6, 'val_4': 5, 'val_5': 0, 'val_6': -7, 'val_7': 1}

# >>> ns2 = Series(labels_numbers)
# >>> ns2
# val_1    3
# val_2   -1
# val_3    6
# val_4    5
# val_5    0
# val_6   -7
# val_7    1
# dtype: int64
# >>>
# >>> ns2.index
# Index(['val_1', 'val_2', 'val_3', 'val_4', 'val_5', 'val_6', 'val_7'], dtype='object')


# >>> Series('abcd')
# 0    abcd
# dtype: object
# >>>
# >>> Series(list('abcd'))
# 0    a
# 1    b
# 2    c
# 3    d
# dtype: object


# >>> Series({1, 2, 3, 4})
# TypeError: 'set' type is unordered

