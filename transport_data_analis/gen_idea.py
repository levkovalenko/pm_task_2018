from csv_parser import Parser
from math import sqrt, acos

a = Parser('transport_data.csv')
a.open()
dots = a.get_data()
zero = []
first = []
second = []
q = []
none = []

with open("answer.txt", "w") as f:
    for dot in dots:
        if dot.label == '-':
            none.append(dot)
        if dot.label == '0':
            zero.append(dot)
        if dot.label == '1':
            first.append(dot)
        if dot.label == '2':
            second.append(dot)
        if dot.label == '?':
            q.append(dot)

    zero.sort()
    first.sort()
    second.sort()

    amount = 0
    for dot in q:
        S = []
        Degrees = []
        Distance = []

        c_log = 111134 # константы для перевода в км
        c_lat = 111319
        for i in range(len(zero) - 1):
            if dot.trans_ts > zero[i].trans_ts:
                dot_1 = zero[i]
                dot_3 = zero[i + 1]
                s_i = abs(0.5 * c_log * c_lat * (
                            (dot_1.log - dot_3.log) * (dot.lat - dot_3.lat) - (dot.log - dot_3.log) * (
                                dot_1.log - dot_3.log)))
                S.append(s_i)

                ax = (dot_1.log - dot.log)
                ay = (dot_1.lat - dot.lat)
                bx = (dot_3.log - dot.log)
                by = (dot_3.lat - dot.lat)
                degr = acos((ax * bx + ay * by) / (sqrt(ax ** 2 + ay ** 2) + sqrt(bx ** 2 + by ** 2)))
                Degrees.append(degr)

                dist = sqrt((ax * c_log) ** 2 + (ay * c_lat) ** 2) + sqrt((bx * c_log) ** 2 + (by * c_lat) ** 2)
                Distance.append(dist)
                break
        for i in range(len(first) - 1):
            if dot.trans_ts > first[i].trans_ts:
                dot_1 = first[i]
                dot_3 = first[i + 1]
                s_i = abs(0.5 * c_log * c_lat * (
                            (dot_1.log - dot_3.log) * (dot.lat - dot_3.lat) - (dot.log - dot_3.log) * (
                                dot_1.log - dot_3.log)))
                S.append(s_i)

                ax = (dot_1.log - dot.log)
                ay = (dot_1.lat - dot.lat)
                bx = (dot_3.log - dot.log)
                by = (dot_3.lat - dot.lat)
                degr = acos((ax * bx + ay * by) / (sqrt(ax ** 2 + ay ** 2) + sqrt(bx ** 2 + by ** 2)))
                Degrees.append(degr)

                dist = sqrt((ax * c_log) ** 2 + (ay * c_lat) ** 2) + sqrt((bx * c_log) ** 2 + (by * c_lat) ** 2)
                Distance.append(dist)
                break
        for i in range(len(second) - 1):
            if dot.trans_ts > second[i].trans_ts:
                dot_1 = second[i]
                dot_3 = second[i + 1]
                s_i = abs(0.5 * c_log * c_lat * (
                            (dot_1.log - dot_3.log) * (dot.lat - dot_3.lat) - (dot.log - dot_3.log) * (
                                dot_1.log - dot_3.log)))
                S.append(s_i)

                ax = (dot_1.log - dot.log)
                ay = (dot_1.lat - dot.lat)
                bx = (dot_3.log - dot.log)
                by = (dot_3.lat - dot.lat)
                degr = acos((ax * bx + ay * by) / (sqrt(ax ** 2 + ay ** 2) + sqrt(bx ** 2 + by ** 2)))
                Degrees.append(degr)

                dist = sqrt((ax * c_log) ** 2 + (ay * c_lat) ** 2) + sqrt((bx * c_log) ** 2 + (by * c_lat) ** 2)
                Distance.append(dist)
                break

        ind = [0, 0, 0]
        ind[0] = S.index(min(S))
        ind[1] = Degrees.index(min(Degrees))
        ind[2] = Distance.index(min(Distance))
        decision = [0, 0, 0]
        for i in range(3):
            if ind[i] == 0:
                decision[0] += 1
            if ind[i] == 1:
                decision[1] += 1
            if ind[i] == 2:
                decision[2] += 1
        res = decision.index(max(decision))
        f.write(f"{res}\n")

#         if ind == 0 :
#
#             f.write("0\n")
#             zero.sort()
#         elif ind == 1 and ind2 == 1:
#             first.append(dot)
#             f.write("1\n")
#             first.sort()
#         elif ind == 2 and ind2 == 2:
#             second.append(dot)
#             f.write("2\n")
#             second.sort()
#         else:
#             f.write("?\n")
#             amount+=1
# print(amount)
