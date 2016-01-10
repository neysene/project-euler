if __name__ == '__main__':
    a = [31,28,31,30,31,30,31,31,30,31,30,31]
    b = [31,29,31,30,31,30,31,31,30,31,30,31]
    t, c = 2, 0
    for i in xrange(1901,2001):
        if i%4 == 0:
            for j in xrange(12):
                t += b[j]
                if t%7 == 0:
                    c += 1
        else:
            for j in xrange(12):
                t += a[j]
                if t%7 == 0:
                    c += 1
    print c
