from math import sqrt

if __name__ == '__main__':
    a, m = [0, 1], 0
    for i in xrange(2,10000):
        s = set([1])
        for j in xrange(2, int(sqrt(i))+1):
            if i%j ==0:
                s.add(j)
                s.add(i/j)
        if sum(s) > 9999:
            a.append(0)
        else:
            a.append(sum(s))

    for k in xrange(2,9999):
        t = a[k]
        if a[t] == k and k!=t:
            m += k
    print m
