from learner import prior, learn, ast, sys
import math
import operator
answe = 0
words_w, weights = learn(100)
print("обучение окончено")
for k in range(50,60):
    with open(f"lemm_text_clear_1000/{k}.txt") as f:
         for line in f:
            article = ast.literal_eval(line)
            text = article[1].split(' ') + article[2].split(' ')
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
                score.update({i: -math.log(prior[i])})
                for j in w:
                    if j in weights[i].keys():
                        score[i] += -math.log(weights[i][j])
            answe += 1 if article[0] == max(score.items(), key=operator.itemgetter(1))[0] else 0
    sys.stdout.write('=')
    sys.stdout.flush()
sys.stdout.write('\n')
sys.stdout.flush()

print(f"{answe/100}%")