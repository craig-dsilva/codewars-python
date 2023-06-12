def double_char(s):
    listedS = list(s)
    doubleCharList = []
    for c in listedS:
        doubleCharList.append(c)
        doubleCharList.append(c)
    doubleCharStr = ''.join(doubleCharList)
    return doubleCharStr
