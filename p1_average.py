def average(a, b, c):
    if a > b:
        if b > c:
            return b
        else:
            if a > c:
                return c
            else:
                return a
    else:
        if a > c:
            return a
        else:
            if b > c:
                return c
            else:
                return b


assert average(1, 8, 9) == 8
assert average(1, 9, 8) == 8
assert average(8, 9, 1) == 8
assert average(9, 8, 1) == 8
assert average(9, 1, 8) == 8
assert average(8, 1, 9) == 8
