from numpy import (
    set_printoptions, 
    float64,
)
from pandas import (
    read_csv, 
    DataFrame,
)
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import (
    root_mean_squared_error as skl_rmse,
    r2_score as skl_r2,
)

from pathlib import Path
from sys import path

set_printoptions(suppress=True)


ModelScore = LinearRegression, float64, float64, float64

def mlr_assessment(
        data: DataFrame,
        target_var: str,
        *depend_vars: str
) -> ModelScore:
    """Выполняет разбивку набора данных на обучающую и тестовую выборки. Обучает и тестирует модель. Возвращает модель и её метрики: среднеквадратичную ошибку, коэффициент детерминации и скорректированный коэффициент детерминации."""
    x = boston.loc[:, depend_vars]
    y = boston[target_var]
    x_train, x_test, y_train, y_test = train_test_split(
        x, y,
        test_size=1/3,
        random_state=1
    )
    # print(x_train.iloc[:2], x_test.iloc[:2], y_train.iloc[:2], y_test.iloc[:2], sep='\n', end='\n\n')
    model = LinearRegression()
    model.fit(x_train, y_train)
    y_predict = model.predict(x_test)
    r2 = float64(skl_r2(y_test, y_predict)).round(2)
    n, k = x_test.shape
    return (
        model, 
        float64(skl_rmse(y_test, y_predict)).round(1), 
        r2, 
        1 - (1 - r2) * ((n - 1) / (n - k - 1)),
    )


data_path = Path(path[0]) / 'boston.csv'
boston = read_csv(data_path, comment='#')

cases = [
    ('LSTAT', 'RM'),
    ('LSTAT', 'RM', 'PTRATIO', 'INDUS', 'TAX'),
    tuple(boston)[:-1],
]
models = []
for case in cases:
    model, rmse, r2, r2_adj = mlr_assessment(boston, 'MEDV', *case)
    models.append(model)
    print(
        'Зависимые переменные:', *case, 
        f'\nRMSE = {rmse}\nR2 = {r2:.0%}\nR2_корр = {r2_adj:.0%}\n'
    )

