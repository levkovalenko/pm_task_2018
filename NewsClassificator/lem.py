import requests


def get_lemm(word):
    resp = requests.get("http://opencorpora.org/dict.php",
                        params={'search_form': word, 'act': 'lemmata'},
                        headers={'Content-Type': 'application/json'},
                        )
    try:
        word = resp.text.split("act")[9].split("] ")[1].split("</a> ")[0]
        object = resp.text.split("act")[9].split("] ")[1].split("</a> ")[1].split('<br/>')[0][1:-1]
        return word,object
    except Exception:
        return word, "NOUN"


if __name__ == "__main__":
    print(get_lemm("df"))
