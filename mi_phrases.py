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


phrases = {"style": set(), "science": set(), "media": set(), "business": set(), "life": set(),
          "travel": set(), "economics": set(), "sport": set(), "culture": set(), "forces": set()}

for theme in themes:
    with open(f"lemm_text_clear_themes/{theme}.txt") as f:
        theme_phrases = set()
        text = []
        for line in f:
            aticle = literal_eval(line)
            headline = aticle[1].strip().split(' ')
            for i in range(len(headline)-1):
                text.append(headline[i]+' '+headline[i+1])
            body = aticle[2].strip().split(' ')

            for i in range(len(body) - 1):
                text.append(body[i] + ' ' + body[i + 1])
        ans = []
        print(f"phrases of {theme} founded")
        print(f"number: {len(text)}")

        unic = set(text)
        for i in unic:
            ans.append((text.count(i),i))
        print("ans is ready")
        ans.sort()
        ans = ans[::-1]
        with open(f"phrase_mi_themes/{theme}.txt", 'w') as file:
            for i in ans:
                file.write(f"{i}\n")
        print("writed")



def log2(x):
    if x == 0:
        return 0
    return log(x, 2)


for theme in themes:
    with open(f"phrase_mi_themes/{theme}.txt", 'w') as f:
        for phrase in list(phrases[theme]):
            N00, N01, N10, N11 = 0, 0, 0, 0
            for doc in all_docs:
                if theme == doc[0] and phrase in doc[1]:
                    N11 += 1
                elif theme != doc[0] and phrase in doc[1]:
                    N10 += 1
                elif theme == doc[0] and phrase not in doc[1]:
                    N01 += 1
                elif theme != doc[0] and phrase not in doc[1]:
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
            f.write(f"{phrase} {mi}\n")

        print(theme)