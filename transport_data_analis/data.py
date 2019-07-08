from math import log


class data():
    def __init__(self, logn, lat, request_ts, trans_ts, label, spec=False):
        self.log = float(logn)
        self.lat = float(lat)
        if spec:
            self.request_ts = log(float(request_ts)-1510000000)
            self.trans_ts = log(float(trans_ts)-1510000000)
        else:
            self.request_ts = float(request_ts)
            self.trans_ts = float(trans_ts)
        self.label = label

    def __str__(self):
        return f"{self.log} {self.lat} {self.label}"

    def __lt__(self, other):
        return self.trans_ts < other.trans_ts

    def dist(self, dot):
        return (self.log-dot.log)**2 + (self.lat-dot.lat)**2 + (log(self.trans_ts,1.8)-log(dot.trans_ts,1.8))**2

    def to_arr(self):
        return f"{self.log},{self.lat},{self.request_ts},{self.trans_ts},{self.label}"

