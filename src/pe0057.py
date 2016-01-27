if __name__ == '__main__':
    n, d, count = 1, 1, 0
    for i in xrange(1000):
        n, d = (n + 2*d), n+d
        if len(str(n)) > len(str(d)):
            count += 1
    print count
