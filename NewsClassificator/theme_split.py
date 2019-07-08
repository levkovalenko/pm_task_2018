from NewsClassificator.reader import read
import sys

reader = read("lemm_text_clear_1000/1.txt")
weight = {"style": {}, "science": {}, "media": {}, "business": {}, "life": {},
          "travel": {}, "economics": {}, "sport": {}, "culture": {}, "forces": {}}
weight_t = {"style": [], "science": [], "media": [], "business": [], "life": [],
          "travel": [], "economics": [], "sport": [], "culture": [], "forces": []}
for i in range(0,60):
    reader = read(f"lemm_text_clear_1000/{i}.txt")
    for _, line in enumerate(reader):
        if _ %100 == 0:
            sys.stdout.write('=')
            sys.stdout.flush()
        if line == "":
            break
        with open(f"lemm_text_clear_themes/{line.theme}.txt", 'a') as f:
            f.write(f"{line.to_text()}\n")
    sys.stdout.write(f'={i}\n')
    sys.stdout.flush()



