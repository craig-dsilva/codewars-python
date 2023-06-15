def series_sum(n):
    if n == 0:
        return "0.00"
    elif n == 1:
        return "1.00"
    else:
        divisor = 1
        i = 1
        sum = 0
        while i < n:
            divisor = divisor + 3
            if i >= 2:
                sum = sum + 1 / divisor
            else:
                sum = 1 + 1 / divisor
            i = i + 1
        return str("%.2f" % round(sum, 2))
