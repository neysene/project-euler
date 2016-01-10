# i can't find a pretty algorithm for this one.
# brute force took less than 3 sec in c but 20 sec in python.
# still in "under a minute" rule.

if __name__ == '__main__':
    m, n = 1, 1
    for a in xrange(500000,1000000):
        k, c = a, 0
        while k > 1:
            if k%2 == 0:
                k /= 2
            else:
                k = (3*k)+1
            c += 1
        if c > m:
            m, n = c, a
    print m, n
