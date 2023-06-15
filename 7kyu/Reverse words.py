def reverse_words(text):
    splitted_text = text.split()
    reversed_text = []
    for word in splitted_text:
        reversed_text.append(word[::-1])
    return " ".join(reversed_text)
