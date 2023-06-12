def smash(words):
    spaced_words = list(map(lambda c: c + " ", words))
    print(spaced_words)
    return "".join(spaced_words).strip()
