from matplotlib import pyplot as plt
from pandas import read_csv, crosstab, Categorical

from itertools import count
from pathlib import Path
from sys import path


data_path = Path(path[0]) / 'HR.csv'

numerical = ['SAT_LVL', 'LE', 'NP', 'AMH', 'TSC']
categorical = ['WA', 'left', 'PROM5', 'DEP', 'SAL']

hr = read_csv(data_path, comment='#')
hr_enc = hr.copy()

hr_enc.columns = numerical + categorical

# >>> hr_enc.info()
# <class 'pandas.core.frame.DataFrame'>
# RangeIndex: 14999 entries, 0 to 14998
# Data columns (total 10 columns):
#  #   Column   Non-Null Count  Dtype
# ---  ------   --------------  -----
#  0   SAT_LVL  14999 non-null  float64
#  1   LE       14999 non-null  float64
#  2   NP       14999 non-null  int64
#  3   AMH      14999 non-null  int64
#  4   TSC      14999 non-null  int64
#  5   WA       14999 non-null  int64
#  6   left     14999 non-null  int64
#  7   PROM5    14999 non-null  int64
#  8   DEP      14999 non-null  object
#  9   SAL      14999 non-null  object
# dtypes: float64(2), int64(6), object(2)
# memory usage: 1.1+ MB

hr_enc['DEP'] = Categorical(
    hr_enc['DEP'], 
    hr_enc['DEP'].unique(),
)
hr_enc['SAL'] = Categorical(
    hr_enc['SAL'],
    ['low', 'medium', 'high'],
    ordered=True
)

dep_to_sel = crosstab(hr_enc['DEP'], hr_enc['SAL'])

# >>> dep_to_sel
# SAL           low  medium  high
# DEP
# sales        2099    1772   269
# accounting    358     335    74
# hr            335     359    45
# technical    1372    1147   201
# support      1146     942   141
# management    180     225   225
# IT            609     535    83
# product_mng   451     383    68
# marketing     402     376    80
# RandD         364     372    51

prom_to_left = crosstab(hr_enc['PROM5'], hr_enc['left'])

# >>> prom_to_left
# left       0     1
# PROM5
# 0      11128  3552
# 1        300    19

prom_to_left_norm = crosstab(hr_enc['PROM5'], hr_enc['left'], normalize='index')

# >>> prom_to_left_norm.round(2)
# left      0     1
# PROM5
# 0      0.76  0.24
# 1      0.94  0.06


hr_enc2 = hr_enc.loc[:, ('WA', 'PROM5', 'SAL', 'left')]
hr_enc2['SAL'] = hr_enc['SAL'].cat.codes

# >>> hr_enc2.corr(method='kendall').round(2)
#          WA  PROM5   SAL  left
# WA     1.00   0.04  0.01 -0.15
# PROM5  0.04   1.00  0.09 -0.06
# SAL    0.01   0.09  1.00 -0.15
# left  -0.15  -0.06 -0.15  1.00


for var in numerical:
    aggr = hr_enc.groupby('left')[var]
    print(aggr.mean().round(2), end='\n\n')

# left
# 0    0.67
# 1    0.44
# Name: SAT_LVL, dtype: float64
# 
# left
# 0    0.72
# 1    0.72
# Name: LE, dtype: float64
# 
# left
# 0    3.79
# 1    3.86
# Name: NP, dtype: float64
# 
# left
# 0    199.06
# 1    207.42
# Name: AMH, dtype: float64
# 
# left
# 0    3.38
# 1    3.88
# Name: TSC, dtype: float64


plt.scatter(
    hr_enc['AMH'], 
    hr_enc['SAT_LVL'].where(hr_enc['left'] == 0),
    color='b'
)
plt.scatter(
    hr_enc['AMH'], 
    hr_enc['SAT_LVL'].where(hr_enc['left'] == 1),
    color='r'
)


