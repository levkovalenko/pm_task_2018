from csv_parser import Parser
from random import randint
from sklearn import svm
from sklearn.model_selection import GridSearchCV
from math import log
from sklearn.model_selection import train_test_split


def svc_param_selection(X, y, nfolds=None):
    Cs = [0.001, 0.01, 0.1, 1, 10,100,1000]
    gammas = [0.001, 0.01, 0.1, 1,10,100,1000]
    param_grid = {'C': Cs, 'gamma' : gammas}
    grid_search = GridSearchCV(svm.SVC(kernel='rbf'), param_grid, cv=3)
    grid_search.fit(X, y)
    print(grid_search.best_params_)


support = svm.SVC(kernel='rbf', C=100, gamma=10)
a = Parser('new_data.csv')
a.open()
dots = a.get_data()

X = []
y = []

TEST = []
a= 1.8
b= 1510000000
for dot in dots:
    if dot.label == '-':
        continue
    if dot.label == '?':
        TEST.append((dot.log, dot.lat, log(dot.trans_ts - b,a), log(dot.request_ts - b,a)))
        continue
    X.append((dot.log, dot.lat, log(dot.trans_ts - b,a), log(dot.request_ts - b,a)))
    y.append(dot.label)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=42)
print(f"train: {len(X_train)}\ntest: {len(X_test)}")
support.fit(X_train, y_train)
print('Accuracy: \n', support.score(X_test, y_test))
pred = support.predict(TEST)
with open("answer2.txt", 'w') as f:
    for item in pred:
        f.write(f"{item}\n")


