import pandas as pd
import sklearn
from sklearn import preprocessing
from sklearn.neighbors import KNeighborsClassifier

data = pd.read_csv('./car.data', ',')

# get the columns and turn it into a list then transform to int values
le = preprocessing.LabelEncoder()
buying = le.fit_transform(list(data["buying"]))
maintenance = le.fit_transform(list(data["maint"]))
door = le.fit_transform(list(data["door"]))
persons = le.fit_transform(list(data["persons"]))
lug_boot = le.fit_transform(list(data["lug_boot"]))
safety = le.fit_transform(list(data["safety"]))
cls = le.fit_transform(list(data["class"]))

# what we are predicting
predict = "class"

x = list(zip(buying, maintenance, door, persons, lug_boot, safety))
y = list(cls)

x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(x, y, test_size=0.1)

model = KNeighborsClassifier(n_neighbors=9)

model.fit(x_train, y_train)
acc = model.score(x_test, y_test)
print(acc)

predicted = model.predict(x_test)

names = ['acc', 'good', 'unacc', 'vgood']
for x in range(len(predicted)):
    print(f'Predicted: {names[predicted[x]]} || Data: {x_test[x]} || Actual: {names[y_test[x]]}')
    print(model.kneighbors([x_test[x]], 9, True))
