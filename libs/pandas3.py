from numpy import array
from pandas import DataFrame

from pprint import pprint
from random import randrange as rr


m1 = array([[1,2,3],[4,5,6],[7,8,9]])

# >>> m1
# array([[1, 2, 3],
#        [4, 5, 6],
#        [7, 8, 9]])

m1_df = DataFrame(m1)

# >>> m1_df
#    0  1  2
# 0  1  2  3
# 1  4  5  6
# 2  7  8  9

# >>> m1_df.index
# RangeIndex(start=0, stop=3, step=1)
# >>>
# >>> m1_df.columns
# RangeIndex(start=0, stop=3, step=1)


numbers_table = {
    f'col_{i}': [rr(-9, 10) for _ in range(12)]
    for i in range(1, 6)
}

# >>> pprint(numbers_table, sort_dicts=False)
# {'col_1': [-2, -2, 0, 8, 1, -1, 0, 9, 1, -4, -2, -5],
#  'col_2': [1, -1, 5, 3, 3, 8, 8, 3, 6, 5, 9, -3],
#  'col_3': [0, 5, -8, 1, 5, -5, -4, 4, 1, 1, 8, -6],
#  'col_4': [4, 8, 5, 2, -3, -4, 4, -2, 5, 1, 6, 0],
#  'col_5': [-7, -2, 5, -6, -8, 7, 7, 7, 4, 9, -8, 3]}


nums_df = DataFrame(numbers_table)

# >>> nums_df
#     col_1  col_2  col_3  col_4  col_5
# 0      -2      1      0      4     -7
# 1      -2     -1      5      8     -2
# 2       0      5     -8      5      5
# 3       8      3      1      2     -6
# 4       1      3      5     -3     -8
# 5      -1      8     -5     -4      7
# 6       0      8     -4      4      7
# 7       9      3      4     -2      7
# 8       1      6      1      5      4
# 9      -4      5      1      1      9
# 10     -2      9      8      6     -8
# 11     -5     -3     -6      0      3

# >>> nums_df.shape
# (12, 5)

# >>> nums_df['col_1']
# 0    -2
# 1    -2
# 2     0
# 3     8
# 4     1
# 5    -1
# 6     0
# 7     9
# 8     1
# 9    -4
# 10   -2
# 11   -5
# Name: col_1, dtype: int64
# >>>
# >>> nums_df['col_4']
# 0     4
# 1     8
# 2     5
# 3     2
# 4    -3
# 5    -4
# 6     4
# 7    -2
# 8     5
# 9     1
# 10    6
# 11    0
# Name: col_4, dtype: int64
# >>>
# >>> type(nums_df['col_1'])
# <class 'pandas.core.series.Series'>


# >>> nums_df.index
# RangeIndex(start=0, stop=12, step=1)
# >>>
# >>> nums_df.columns
# Index(['col_1', 'col_2', 'col_3', 'col_4', 'col_5'], dtype='object')

row_lbls = [f'row_{i}' for i in range(1, 13)]

# >>> nums_df.index = row_lbls
# >>> nums_df
#         col_1  col_2  col_3  col_4  col_5
# row_1      -2      1      0      4     -7
# row_2      -2     -1      5      8     -2
# row_3       0      5     -8      5      5
# row_4       8      3      1      2     -6
# row_5       1      3      5     -3     -8
# row_6      -1      8     -5     -4      7
# row_7       0      8     -4      4      7
# row_8       9      3      4     -2      7
# row_9       1      6      1      5      4
# row_10     -4      5      1      1      9
# row_11     -2      9      8      6     -8
# row_12     -5     -3     -6      0      3
# >>> 
# >>> nums_df.index
# Index(['row_1', 'row_2', 'row_3', 'row_4', 'row_5', 'row_6', 'row_7', 'row_8',
#        'row_9', 'row_10', 'row_11', 'row_12'],
#       dtype='object')

# >>> nums_df['row_1']
# KeyError: 'row_1'

# >>> nums_df.loc
# <pandas.core.indexing._LocIndexer object at 0x000001F2AA8C7C00>
# >>>
# >>> nums_df.iloc
# <pandas.core.indexing._iLocIndexer object at 0x000001F2AA8E1400>

# >>> nums_df.loc['row_1', :]
# col_1   -2
# col_2    1
# col_3    0
# col_4    4
# col_5   -7
# Name: row_1, dtype: int64
# >>> 
# >>> nums_df.iloc[0, :]
# col_1   -2
# col_2    1
# col_3    0
# col_4    4
# col_5   -7
# Name: row_1, dtype: int64

# >>> nums_df.loc['row_5':'row_10', 'col_3':'col_5']
#         col_3  col_4  col_5
# row_5       5     -3     -8
# row_6      -5     -4      7
# row_7      -4      4      7
# row_8       4     -2      7
# row_9       1      5      4
# row_10      1      1      9
# >>>
# >>>
# >>> nums_df.loc[:, ('col_1', 'col_3', 'col_4')]
#         col_1  col_3  col_4
# row_1      -2      0      4
# row_2      -2      5      8
# row_3       0     -8      5
# row_4       8      1      2
# row_5       1      5     -3
# row_6      -1     -5     -4
# row_7       0     -4      4
# row_8       9      4     -2
# row_9       1      1      5
# row_10     -4      1      1
# row_11     -2      8      6
# row_12     -5     -6      0

