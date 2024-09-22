from numpy import float64
from pandas import (
    crosstab, 
    Categorical,
    DataFrame,
    MultiIndex,
    read_csv, 
)
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

from pathlib import Path
from sys import path


data_path = Path(path[0]) / 'HR.csv'

hr = read_csv(data_path, comment='#')
hr_enc = hr.copy()
hr_enc.columns = ['SAT_LVL', 'LE', 'NP', 'AMH', 'TSC', 'WA', 'left', 'PROM5', 'DEP', 'SAL']

hr_enc['SAL'] = Categorical(hr_enc['SAL'], ['low', 'medium', 'high'], ordered=True).codes


x = hr_enc.loc[:, ('SAT_LVL', 'AMH', 'TSC', 'WA', 'SAL', 'PROM5')]
y = hr_enc['left']

x_train, x_test, y_train, y_test = train_test_split(
    x, y,
    test_size=1/3,
    random_state=1
)

x_num = x_train.loc[:, ('SAT_LVL', 'AMH', 'TSC')]
x_train.loc[:, ('SAT_LVL', 'AMH', 'TSC')] = (x_num - x_num.mean()) / x_num.std()

model = LogisticRegression()
model.fit(x_train, y_train)

y_pred = model.predict(x_test)

# left = 0 — negative
# left = 1 — positive
TP, TN, FP, FN = 0, 0, 0, 0
for actual, predict in zip(y_test.to_numpy(), y_pred):
    if actual and predict:
        TP += 1
    elif not actual and not predict:
        TN += 1
    elif actual and not predict:
        FN += 1
    elif not actual and predict:
        FP += 1

conf_matrix = DataFrame(
    [[TN, FP], [FN, TP]], 
    columns=MultiIndex.from_tuples([('прогноз', 'остался'), ('прогноз', 'ушёл')]),
    index=MultiIndex.from_tuples([('факт', 'остался'), ('факт', 'ушёл')])
)

