from csv_parser import Parser
import gmplot

a = Parser('transport_data.csv')
a.open()
dots = a.get_data()

gmap = gmplot.GoogleMapPlotter(59.95, 30.3, 12)


zero = []
first = []
second = []
q = []
for dot in dots:
    if dot.label == '0':
        zero.append(dot)
    if dot.label == '1':
        first.append(dot)
    if dot.label == '2':
        second.append(dot)
    if dot.label == '?':
        q.append(dot)


lats, logs = [], []
for dot in zero:
    lats.append(dot.lat)
    logs.append(dot.log)

gmap.scatter(lats, logs, 'red', marker=False)

lats, logs = [], []
for dot in first:
    lats.append(dot.lat)
    logs.append(dot.log)

gmap.scatter(lats, logs, 'pink', marker=False)

lats, logs = [], []
for dot in second:
    lats.append(dot.lat)
    logs.append(dot.log)

gmap.scatter(lats, logs, 'cornflowerblue', marker=False)

lats, logs = [], []
for dot in q:
    lats.append(dot.lat)
    logs.append(dot.log)

gmap.scatter(lats, logs, 'black', marker=False)

gmap.draw("mymap.html")

print(len(q))

"""
label 0 - маршрут 5
label 1 - маршрут 11 
label 2 - маршрут 7
"""
