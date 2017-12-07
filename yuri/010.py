def primesieve(n):
    l = list(range(n))
    for i in range(2, int(n**.5+1)):
        if l[i]:
           l[i**2::i] = [0]*((n-1-i**2)//i + 1)
    return [x for x in l if x]

print(sum(primesieve(2000000)))
