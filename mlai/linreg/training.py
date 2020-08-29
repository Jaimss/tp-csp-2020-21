import pickle

import sklearn
from sklearn import linear_model


def train_model(x, y):
    best = 0
    for _ in range(500):
        x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(x, y, test_size=0.1)

        linear = linear_model.LinearRegression()

        linear.fit(x_train, y_train)
        acc = linear.score(x_test, y_test)
        print(acc)

        if acc > best:
            best = acc
            with open("studentmodel.pickle", "wb") as f:
                pickle.dump(linear, f)


def load_model():
    pickle_in = open("studentmodel.pickle", "rb")
    linear = pickle.load(pickle_in)
    return linear
