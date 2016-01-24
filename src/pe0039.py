def gcd(i, j):
    while j:      
        i, j = j, i%j
    return i

def lcm(i, j):
    return i*j / gcd(i, j)

if __name__ == '__main__':
    a, maxlcm, t, result = set(), 1, 0, []
    for i in xrange(2, 100):
        k = (1 if i%2 == 0 else 2)
        for j in xrange(k, i, 2):
            if gcd(i, j) == 1:
                a.add(2*i*(i+j))
    sorteda = sorted(a)

    while maxlcm <= 1000:
        maxlcm = lcm(maxlcm, sorteda[t])
        result.append(maxlcm)
        t += 1

    print 'Problem 39 - Answer is ', result[-2] 
