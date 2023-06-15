def to_jaden_case(string):
    listed_words = string.split()
    capitalized_words = []
    for word in listed_words:
        capitalized_words.append(word.capitalize())
    return " ".join(capitalized_words)
