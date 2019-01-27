from lem import get_lemm
import re
import ast

text_utils = {'PREP','CONJ','INTJ','PRED','PRCL','NPRO'}


class News(object):
    def __init__(self, line):
        try:
            line = ast.literal_eval(line[:-1])
            theme, headline, text = line[0], line[1], line[2]
        except Exception:
            headline, text = line.split('\t')
        self.headline = headline
        self.text = text

    def __str__(self):
        return f"{self.theme} {self.headline}"

    def clear_text(self, reg=None):
        self.headline = self.headline.lower()
        self.text = self.text.lower()
        if reg is None:
            reg = re.compile('[^а-яa-z ]')
        self.text = reg.sub('', self.text)
        self.headline = reg.sub('', self.headline)

    def lemmatization(self):
        self.clear_text()
        text = ''
        headline = ''
        for word in self.headline.split(' '):
            word = get_lemm(word)
            if word[1] not in text_utils:
                headline += word[0] + ' '
        for word in self.text.split(' '):
            word = get_lemm(word)
            if word[1] not in text_utils:
                text += word[0] + ' '
        self.headline = headline
        self.text = text

    def to_text(self):
        return [self.headline, self.text]
