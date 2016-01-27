def digital_sum(a):
    s = 0
    while a > 0:
        s += a%10
        a /= 10
    return s

if __name__ == '__main__':
    m = 0
    a = set()
    for i in xrange(1, 100, 1):
        k = i
        for j in xrange(99):
            k = k*i
            a.add(digital_sum(k))
    print max(a)
