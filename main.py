from matrix_of_words import prior, words_w, ast,weights
import math
import operator
answe = 0
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
                score.update(dict.fromkeys([i], (-math.log(prior[i]))))

                for j in w:
                    if j in weights[i]:
                        #print(weights[i][j])
                        score[i] += -math.log(weights[i][j])
            #print(article[0], max(score.items(), key=operator.itemgetter(1))[0])
            answe += 1 if article[0] == max(score.items(), key=operator.itemgetter(1))[0] else 0
            #'''
            if article[0] != max(score.items(), key=operator.itemgetter(1))[0]:
                print(max(score.items(), key=operator.itemgetter(1))[0], article[0])
                print(article[1])
                print(score)
            #'''
print(f"{answe/100}%")
