from matrix_of_words import prior, learn, ast, sys
import math
import operator
answe = 0
words_w, weights = learn(10000)
print("обучение окончено")
with open("answer.txt", 'w') as ans:
    with open(f"test_clear/test.txt") as f:

        for line in f:
            article = ast.literal_eval(line)
            text = article[0].split(' ') + article[1].split(' ')
            score = dict()
            V = set()
            [V.update(set(x)) for x in words_w.values()]
            V -= {''}
            w = list()
            # 	w.update(set(body) & V)

            for i in text:
                if i in V:
                    w.append(i)
            for i in words_w.keys():
                # 			score.update(i=math.log(prior[i]))
                score.update({i: math.log(prior[i])})
                for j in w:
                    if j in weights[i].keys():
                        score[i] += math.log(weights[i][j])
            ans.write(f"{max(score.items(), key=operator.itemgetter(1))[0]}\n")
    sys.stdout.write('=')
    sys.stdout.flush()
sys.stdout.write('\n')
sys.stdout.flush()

print(f"{answe/600}%")