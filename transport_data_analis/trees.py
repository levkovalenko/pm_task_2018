from sklearn import tree
from csv_parser import Parser
from math import log
from sklearn.model_selection import train_test_split



decision = tree.DecisionTreeRegressor( min_impurity_decrease=1e-7)


a = Parser('transport_data.csv')
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
decision.fit(X, y)
print('Accuracy: \n', decision.score(X_test, y_test))
pred = decision.predict(TEST)
with open("answertrees.txt", 'w') as f:
    for item in pred:
        f.write(f"{item}\n")