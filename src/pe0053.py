def ret_count(a):
    n, d, t, k = a, 1, a-1, 2
    while True:
        if n/d > 1000000:
            break
        n *= t
        t -= 1
        d *= k
        k += 1
    return t-k+2

if __name__ == '__main__':
    sm = 0
    for i in xrange(23,101):
        sm += ret_count(i)
    print sm
