for a in range(1, 1000):
    for b in range(a, 1000):
        c = 1000 - a - b
        if a*a + b*b == c*c:
            print(a*b*c)
            break


def pythagarean(n):
    for a in range(1, n+1):
        for b in range(a, n+1):
            s = a**2 + b **2
            c = int(s**.5)
            if (s == c**2) and (c <= n):
                yield (a,b,c)

for a,b,c in pythagarean(1000):
    if a + b + c == 1000:
        print(a*b*c)
        break
