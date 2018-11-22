from matrix_of_words import prior, words_w, ast,weights
import math
import operator
answe = 0
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
                score.update(dict.fromkeys([i], (-math.log(prior[i]))))

                for j in w:
                    if j in weights[i]:
                        #print(weights[i][j])
                        score[i] += -math.log(weights[i][j])
            #print(article[0], max(score.items(), key=operator.itemgetter(1))[0])
            ans.write(f"{max(score.items(), key=operator.itemgetter(1))[0]}\n")

