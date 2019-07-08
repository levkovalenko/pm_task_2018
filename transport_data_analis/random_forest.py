from sklearn.ensemble import ExtraTreesClassifier as RandomForestClassifier
from csv_parser import Parser
from math import log
from sklearn.model_selection import train_test_split
from matplotlib import pyplot as plt
import numpy as np

decision = RandomForestClassifier(criterion='gini', n_estimators=20000, min_samples_leaf=1,
                                  max_features=4,bootstrap=True, n_jobs=-1,warm_start=True)
a = Parser('transport_data.csv')
a.open()
dots = a.get_data()

X = []
y = []

TEST = []
a = 10
c = 17
b = 1510000000
for dot in dots:
    if dot.label == '-':
        continue
    if dot.label == '?':
        TEST.append((dot.log, dot.lat, dot.trans_ts, dot.request_ts))
        continue
    X.append((dot.log, dot.lat, dot.trans_ts, dot.request_ts))
    y.append(dot.label)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=42)
decision.fit(X, y)
print('Accuracy: \n', decision.score(X_test, y_test))

pred = decision.predict(TEST)
print(decision.feature_importances_)

with open("answerforest3.txt", 'w') as f:
    for item in pred:
        f.write(f"{item}\n")