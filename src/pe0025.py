def fibo(a, b, c, hane):
    i, elde = 0, 0
    while i<hane:
        c[i] = a[i] + b[i] + elde
        elde = 0
        if c[i] > 9:
            c[i] = c[i]%10
            elde += 1
        i += 1
        if hane == i and elde == 1:
            hane += 1
    return hane, a, b, c

if __name__ == '__main__':
    a, b, c, hane, seq = [0] * 1005, [0] * 1005, [0] * 1005, 1, 3
    a[0], b[0] = 1, 2
    while hane < 1000:
        if seq%3 == 0:
            hane, a, b, c = fibo(a, b, c, hane)
        elif seq%3 == 1:
            hane, b, c, a = fibo(b, c, a, hane)
        else:
            hane, c, a, b = fibo(c, a, b, hane)
        seq += 1
    print seq

