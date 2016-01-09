def primelist(n):
    sieve = [True] * (n/2)
    for i in xrange(3,int(n**0.5)+1,2):
        if sieve[i/2]:
            sieve[i*i/2::i] = [False] * ((n-i*i-1)/(2*i)+1)
    return [2] + [2*i+1 for i in xrange(1,n/2) if sieve[i]]

def divisors(n, p):
    a, i, s = [], 0, 1
    try:
        while n > 1 or n>=p[i]:
            if n%p[i] == 0:
                a.append(2)
                n /= p[i]
                while n%p[i] == 0:
                    a[-1] += 1
                    n /= p[i]
            i += 1
    except IndexError:
        pass
    for k in a:
        s *= k
    return s

if __name__ == '__main__':
    p, j, d, s = primelist(1000), 1, 2, 1
    while s < 500:
        j += d
        d += 1
        s = divisors(j, p)
    print j
