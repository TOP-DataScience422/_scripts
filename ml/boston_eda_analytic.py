from pandas import read_csv

from pathlib import Path
from sys import path


data_path = Path(path[0]) / 'boston.csv'


boston = read_csv(data_path, comment='#')

# численные характеристики признаков
boston_props = boston.describe()
print(boston_props.round(2), end='\n\n')

# взаимосвязи между признаками
boston_corr = boston.corr().round(2)
print(boston_corr, end='\n\n')

