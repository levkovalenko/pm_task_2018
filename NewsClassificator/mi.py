from ast import literal_eval
from math import log
import sys

themes = ["style", "science", "media", "business", "life",
          "travel", "economics", "sport", "culture", "forces"]

all_docs = []
for theme in themes:
    with open(f"lemm_text_clear_themes/{theme}.txt") as f:
        for line in f:
            aticle = literal_eval(line)
            one_new = [aticle[0]]
            text = aticle[1].split(' ') + aticle[2].split(' ')
            text = set(text) - {''}
            one_new.append(text)
            all_docs.append(one_new)
        sys.stdout.write(f"{theme}\n")
        sys.stdout.flush()
print(len(all_docs))


terms = {"style": set(), "science": set(), "media": set(), "business": set(), "life": set(),
          "travel": set(), "economics": set(), "sport": set(), "culture": set(), "forces": set()}

for theme in themes:
    with open(f"lemm_text_clear_themes/{theme}.txt") as f:
        theme_terms = set()
        for line in f:
            aticle = literal_eval(line)
            text = aticle[1].split(' ') + aticle[2].split(' ')
            text = set(text) - {''}
            theme_terms = theme_terms.union(text)
        terms[theme] = theme_terms
        sys.stdout.write(f"unic terms of {theme}: {len(terms[theme])}\n")


def log2(x):
    if x == 0:
        return 0
    return log(x, 2)


for theme in themes:
    with open(f"mi_themes/{theme}.txt", 'w') as f:
        for term in list(terms[theme]):
            N00, N01, N10, N11 = 0, 0, 0, 0
            for doc in all_docs:
                if theme == doc[0] and term in doc[1]:
                    N11 += 1
                elif theme != doc[0] and term in doc[1]:
                    N10 += 1
                elif theme == doc[0] and term not in doc[1]:
                    N01 += 1
                elif theme != doc[0] and term not in doc[1]:
                    N00 += 1
            N = N11 + N01 + N10 + N00
            N1x = N11 + N10
            Nx1 = N11 + N01
            Nx0 = N00 + N10
            N0x = N00 + N01
            if N11 == 0:
                continue
            mi = (((N11 / N) * log2((N * N11) / (N1x * Nx1))) + ((N01 / N) * log2((N * N01) / (N0x * Nx1))) + (
                        (N10 / N) * log2((N * N10) / (N1x * Nx0))) + ((N00 / N) * log2((N * N00) / (N0x * Nx0))))
            f.write(f"{term} {mi}\n")

        print(theme)
