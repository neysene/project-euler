if __name__ == '__main__':
    a = set()
    for i in xrange(2,101):
        for j in xrange(2,101):
            a.add(i**j)
    print len(a)
