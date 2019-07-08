import ast
import sys

themes = ["style", "science", "media", "business", "life",
          "travel", "economics", "sport", "culture", "forces"]

words_w = {"style": [], "science": [], "media": [], "business": [], "life": [],
          "travel": [], "economics": [], "sport": [], "culture": [], "forces": []}

num = 1

prior = {"style": 1147 / num, "science": 8657 / num, "media": 8629 / num,
         "business": 2099 / num, "life": 8083 / num, "travel": 2099 / num,
         "economics": 8545 / num, "sport": 8510 / num, "culture": 8405 / num,
         "forces": 4758 / num}

weights = {"style": {}, "science": {}, "media": {}, "business": {}, "life": {},
          "travel": {}, "economics": {}, "sport": {}, "culture": {}, "forces": {}}


def learn(number):
    all_terms = {}
    for theme in themes:
        with open(f"mi_themes/{theme}.txt") as f:
            terms = []
            for line in f:
                term, mi = line.split(' ')
                terms.append((float(mi), term))
            terms.sort()
            terms = terms[::-1]
            terms = terms[:number]
        words_w[theme] = [termin for _, termin in terms]
        [all_terms.update({t: w*0.5*10**4}) for w, t in terms]
    for theme in themes:
        with open(f"lemm_text_clear_themes/{theme}.txt") as f:
            weights[theme].clear()
            text = []
            for line in f:
                article = ast.literal_eval(line)
                text += article[1].split(' ') + article[2].split(' ')
                text.remove('')
            tmp = words_w[theme]
            sum = 0
            for i, word in enumerate(tmp):
                sum += text.count(word)+1
            for i, word in enumerate(tmp):
                weights[theme].update({word: (text.count(word)+1)+all_terms[word]})
        sys.stdout.write('=')
        sys.stdout.flush()
    sys.stdout.write('\n')
    sys.stdout.flush()
    return words_w, weights


if __name__ == "__main__":
    number = 25
    a, b = learn(number)
    print(a)
    print(b)
