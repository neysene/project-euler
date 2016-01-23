if __name__ == '__main__':
    a, finalsum = [], 0
    for i in xrange(10):
        a.append(i**5)

    for i in xrange(4):
        for j in xrange(10):
            for k in xrange(10):
                for l in xrange(10):
                    for m in xrange(10):
                        for n in xrange(10):
                            if a[i]+a[j]+a[k]+a[l]+a[m]+a[n] == int(str(i)+str(j)+str(k)+str(l)+str(m)+str(n)):
                                finalsum += a[i]+a[j]+a[k]+a[l]+a[m]+a[n]
    print finalsum-1
