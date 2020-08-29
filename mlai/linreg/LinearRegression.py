import numpy as np
import pandas as pd
import sklearn

from linreg.methods import (load_model, show_plot)

# read the data from the csv and load it into what we need
data = pd.read_csv('student-mat.csv', sep=';')
data = data[["G1", "G2", "G3", "studytime", "failures", "absences"]]

# we are predicting G3
predict = "G3"  # attr name

# train
x = np.array(data.drop([predict], 1))
y = np.array(data[predict])
x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(x, y, test_size=0.1)

# train_model(x, y)
linear = load_model()

show_plot(data, 'absences')
