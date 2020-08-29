import matplotlib.pyplot as pyplot
import numpy as np
import pandas as pd
import sklearn
from matplotlib import style

from linreg.training import (load_model)

data = pd.read_csv('student-mat.csv', sep=';')
data = data[["G1", "G2", "G3", "studytime", "failures", "absences"]]

predict = "G3"  # attr name

x = np.array(data.drop([predict], 1))
y = np.array(data[predict])
x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(x, y, test_size=0.1)

# train_model(x, y)
linear = load_model()

p = 'absences'
style.use("ggplot")
pyplot.scatter(data[p], data['G3'])
pyplot.xlabel(p)
pyplot.ylabel('Final Grade')
pyplot.show()
