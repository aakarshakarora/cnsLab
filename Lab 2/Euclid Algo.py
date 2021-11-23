def fx(a, b):
    if a == 0:
        return b, 0, 1

    gcd, x1, y1 = fx(b % a, a)

    x = y1 - (b // a) * x1
    y = x1

    return gcd, x, y


# Driver code
a, b = map(int, input().split())
g, x, y = fx(a, b)
print("Output is ", g)
