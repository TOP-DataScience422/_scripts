from matplotlib import pyplot as plt
from pandas import DataFrame
from scipy.io.arff import loadarff
from sklearn.metrics import confusion_matrix
from sklearn.metrics import ConfusionMatrixDisplay
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

from pathlib import Path
from sys import path


data_path = Path(path[0]) / 'blood-transfusion-service-center.arff'
with open(data_path, encoding='utf-8') as filein:
    data_raw = loadarff(filein)


data = DataFrame(data_raw[0])

data['V1'] = data['V1'].astype(int)
data['V2'] = data['V2'].astype(int)
data['V3'] = data['V3'].astype(int)
data['V4'] = data['V4'].astype(int)

data['Class'] = data['Class'].where(data['Class'] != b'1', 0)
data['Class'] = data['Class'].where(data['Class'] != b'2', 1).astype(int)


x = data.iloc[:, :-1]
y = data.iloc[:, -1]
x_train, x_test, y_train, y_test = train_test_split(
    x, y,
    test_size=1/3,
    random_state=1,
)


model = DecisionTreeClassifier()
model.fit(x_train, y_train)

y_pred = model.predict(x_test)


result = DataFrame({
    'actual': y_test,
    'predicted': y_pred,
    'match': y_test == y_pred,
})

# >>> result['match'].value_counts(normalize=True).round(2)
# match
# True     0.72
# False    0.28
# Name: proportion, dtype: float64

# >>> print(confusion_matrix(y_test, y_pred))
# [[160  27]
#  [ 41  22]]


# ConfusionMatrixDisplay.from_predictions(y_test, y_pred)
# plt.show()

