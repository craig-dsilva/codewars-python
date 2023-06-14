def century(year):
    if year <= 100:
        return 1
    elif year > 100 and year < 1000:
        return int(str(year)[0:1]) + 1
    elif str(year)[2:] == '00':
        return int(str(year)[0:2])
    else:
        return int(str(year)[0:2]) + 1
