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
none = []
with open("new_data1.csv", "w") as f:
    f.write("log,lat,request_ts,trans_ts,label\n")
    for dot in dots:
        if dot.label == '-':
            none.append(dot)
        if dot.label == '0':
            zero.append(dot)
            f.write(f"{dot.to_arr()}\n")
        if dot.label == '1':
            first.append(dot)
            f.write(f"{dot.to_arr()}\n")
        if dot.label == '2':
            second.append(dot)
            f.write(f"{dot.to_arr()}\n")
        if dot.label == '?':
            q.append(dot)
            f.write(f"{dot.to_arr()}\n")

    dots1 = zero+first+second


    for dot in none:
        near_dot = None
        dist = 100000000
        for item in dots1:
            if dot.dist(item) < dist:
                dist = dot.dist(item)
                near_dot = item
        dot.label = near_dot.label
        dots1.append(dot)
        if dot.label == '0':
            zero.append(dot)
            f.write(f"{dot.to_arr()}\n")
        if dot.label == '1':
            first.append(dot)
            f.write(f"{dot.to_arr()}\n")
        if dot.label == '2':
            second.append(dot)
            f.write(f"{dot.to_arr()}\n")

