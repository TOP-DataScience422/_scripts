from numpy import float64
from pandas import (
    read_csv, 
    crosstab, 
    Categorical,
    DataFrame,
    MultiIndex,
)
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    confusion_matrix,
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
)
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
x_train['TSC'] = x_train['TSC'].astype(float64)
x_train['AMH'] = x_train['AMH'].astype(float64)
x_train.loc[:, ('SAT_LVL', 'AMH', 'TSC')] = (x_num - x_num.mean()) / x_num.std()

model = LogisticRegression()
model.fit(x_train, y_train)

y_pred = model.predict(x_test)


# left = 0 — остался — negative
# left = 1 — ушёл — positive


# n = 10
#                      прогноз     
#                |—————————|————————|
#                | остался |  ушёл  |
#      |—————————|—————————|————————|
#      | остался |  7 (TN) | 1 (FP) | -
# факт |—————————|—————————|————————|
#      |  ушёл   |  1 (FN) | 1 (TP) | +
#      |—————————|—————————|————————|
#                     -        +
# 
#                 TN + TP            7 + 1
# accuracy = ————————————————— = ————————————— = 0.80
#            TN + FP + TP + FN   7 + 1 + 1 + 1
# 
#                TP       1
# precision = ——————— = ————— = 0.5
#             TP + FP   1 + 1
# 
#             TP       1
# recall = ——————— = ————— = 0.5
#          TP + FN   1 + 1
# 
#                 2             2 * precision * recall   2 * 0.5 * 0.5
# f1 = —————————————————————— = —————————————————————— = ————————————— = 0.5
#      1/precision + 1/recall     precision + recall       0.5 + 0.5


# n = 100
#                      прогноз     
#                |—————————|————————|
#                | остался |  ушёл  |
#      |—————————|—————————|————————|
#      | остался | 80 (TN) | 4 (FP) | -
# факт |—————————|—————————|————————|
#      |  ушёл   |  9 (FN) | 7 (TP) | +
#      |—————————|—————————|————————|
#                     -        +
# 
#                 TN + TP            80 + 7
# accuracy = ————————————————— = —————————————— = 0.87
#            TN + FP + TP + FN   80 + 4 + 7 + 9
# 
#                TP       7
# precision = ——————— = ————— = 0.64
#             TP + FP   7 + 4
# 
#             TP       7
# recall = ——————— = ————— = 0.438
#          TP + FN   7 + 9
# 
#                 2             2 * precision * recall   2 * 0.64 * 0.438
# f1 = —————————————————————— = —————————————————————— = ———————————————— = 0.52
#      1/precision + 1/recall     precision + recall       0.64 + 0.438


conf_matrix = DataFrame(
    confusion_matrix(y_test, y_pred), 
    columns=MultiIndex.from_tuples([('прогноз', 'остался'), ('прогноз', 'ушёл')]),
    index=MultiIndex.from_tuples([('факт', 'остался'), ('факт', 'ушёл')])
)

# >>> conf_matrix
#              прогноз
#              остался  ушёл
# факт остался       0  3788
#      ушёл          0  1212
# >>> 
# >>> accuracy_score(y_test, y_pred)
# 0.2424
# >>>
# >>> precision_score(y_test, y_pred)
# np.float64(0.2424)
# >>>
# >>> recall_score(y_test, y_pred)
# np.float64(1.0)
# >>>
# >>> f1_score(y_test, y_pred)
# np.float64(0.39021249195106245)

