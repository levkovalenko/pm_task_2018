from NewsClassificator.reader import read
import sys


reader = read("news_test.txt")

l = open("test_clear/test.txt", 'w')
for _, line in enumerate(reader):
    if line == "":
        break
    line.lemmatization()
    l.write(f"{line.to_text()}\n")
    if _ % 1000 == 0:
        sys.stdout.write('=')
        sys.stdout.flush()

l.close()
