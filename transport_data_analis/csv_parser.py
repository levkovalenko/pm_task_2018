import csv
import logging
from data import data


class Parser:
    def __init__(self, filename, **kwargs):
        self.filename = filename
        self.reader = None
        self.file = None
        self.__date = []

    def open(self):
        try:
            self.file = open(self.filename, mode='r')
            logging.info(f"open {self.filename} file")
            self.reader = csv.DictReader(self.file)
            self.__read()
            logging.info(f"read all information from {self.filename}")
        except Exception as e:
            logging.fatal(e)
            raise Exception(e)

    def __read(self):
        line_count = 0
        for row in self.reader:
            if line_count == 0:
                line_count = 1
            place = data(row['log'], row['lat'], row['request_ts'], row['trans_ts'], row['label'])
            try:
                self.__date.append(place)
            except Exception as e:
                print(e)

    def get_data(self):
        return self.__date

    def close(self):
        if self.file:
            self.file.close()
        else:
            logging.fatal("No file to close")
            raise Exception('No file to close')


class Parser1(Parser):
    def __read(self):
        line_count = 0
        for row in self.reader:
            if line_count == 0:
                line_count = 1
            place = data(row['log'], row['lat'], row['request_ts'], row['trans_ts'], row['label'], spec=True)
            try:
                self.__date.append(place)
            except Exception as e:
                print(e)
