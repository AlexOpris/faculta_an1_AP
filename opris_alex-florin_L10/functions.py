def gcd(a, b):
    if a < 0 or b < 0:
        raise ValueError("Numbers must be possitive")
    elif a == b:
        return b
    elif a > b:
        return gcd(a - b, b)
    else:
        return gcd(a, b - a)

def power(a, x):
    if x < 0:
        raise ValueError("Power must be possitive")
    elif x == 0:
        return 1
    elif x == 1:
        return a
    else:
        return a * power(a, x-1)
