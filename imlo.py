from uzwords import words
from difflib import get_close_matches

def wordcheck(word,words = words):
    word = word.lower()
    matches = set(get_close_matches(word,words))
    available = False

    for match in matches:
        available = True
        matches = match


    return {'availabe':available,'matches':matches}

print(wordcheck('абад'))