def count_sheep(n):
    string = ""
    i = 1
    while i <= n:
        string = string + str(i) + " sheep..."
        i = i + 1
    return string
