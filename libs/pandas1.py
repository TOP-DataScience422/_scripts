from pandas import Series

from pprint import pprint


numbers = [3, -1, 6, 5, 0, -7, 1]
ns = Series(numbers)

# >>> ns
# 0    3
# 1   -1
# 2    6
# 3    5
# 4    0
# 5   -7
# 6    1
# dtype: int64

# >>> ns.name
# >>> type(ns.name)
# <class 'NoneType'>
# >>>
# >>> ns.name = 'rand_numbers'
# >>> ns
# 0    3
# 1   -1
# 2    6
# 3    5
# 4    0
# 5   -7
# 6    1
# Name: rand_numbers, dtype: int64

# >>> ns[0]
# np.int64(3)
# >>>
# >>> type(ns[0])
# <class 'numpy.int64'>
# >>> 
# >>> ns.index
# RangeIndex(start=0, stop=7, step=1)

row_lbls = [f'val_{i}' for i in range(1, len(ns)+1)]

# >>> row_lbls
# ['val_1', 'val_2', 'val_3', 'val_4', 'val_5', 'val_6', 'val_7']

# >>> ns.index = row_lbls
# >>> ns.index
# Index(['val_1', 'val_2', 'val_3', 'val_4', 'val_5', 'val_6', 'val_7'], dtype='object')
# >>>
# >>> ns
# val_1    3
# val_2   -1
# val_3    6
# val_4    5
# val_5    0
# val_6   -7
# val_7    1
# Name: rand_numbers, dtype: int64
# >>>
# >>> ns['val_1']
# np.int64(3)

# >>> ns.iloc
# <pandas.core.indexing._iLocIndexer object at 0x00000286DCFD61C0>
# >>>
# >>> ns.iloc[0]
# np.int64(3)
# >>>
# >>> ns.iloc[:3]
# val_1    3
# val_2   -1
# val_3    6
# Name: rand_numbers, dtype: int64

