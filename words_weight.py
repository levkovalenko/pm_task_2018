import ast

themes = ["style", "science", "media", "business", "life",
          "travel", "economics", "sport", "culture", "forces"]

for theme in themes:
    with open(f"lemm_text_clear_themes/{theme}.txt", 'r') as file:
        lines = []
        for line in file:
            lines.append(ast.literal_eval(line))

    words = {}
    for line in lines:
        for word in line[2].split(' '):
            if word in words:
                words[word] += 1
            else:
                words.update({word:1})

    texts = []
    for k, v in words.items():
        texts.append((v,k))
    texts.sort(reverse=True)

    with open(f"words_weight_texts/{theme}.txt", 'w') as f:
        for word in texts:
            if word[0] < 20:
                continue
            f.write(f"{word[1]} {word[0]}\n")
