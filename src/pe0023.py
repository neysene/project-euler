# takes around 3.5 sec
# i wrote algorithms for finding divisors and abundants
# but they took much more time than brute force
# (i facepalmed myself)

def brute_force():
    a = []
    for i in xrange(12, 28123):
        t = set([1])
        s = int(i**0.5) + 1
        for j in xrange(2, s):
            if i%j == 0:
                t.add(j)
                t.add(i/j)
        if sum(t) > i:
            a.append(i)
    return a
                

if __name__ == '__main__':
    ab, l = brute_force(), set([])
    for i in xrange(len(ab)):
        for j in xrange(i,len(ab)):
            if (ab[i] + ab[j]) > 28123:
                break
            else:
                l.add(ab[i] + ab[j])
    print 28123*(28123+1)/2 - sum(l)

