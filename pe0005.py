def primelist(n):
    sieve = [True] * (n/2)
    for i in xrange(3,int(n**0.5)+1,2):
        if sieve[i/2]:
            sieve[i*i/2::i] = [False] * ((n-i*i-1)/(2*i)+1)
    return [2] + [2*i+1 for i in xrange(1,n/2) if sieve[i]]

if __name__ == '__main__':
    p, i, t, s = primelist(10), 0, 2, 1
    for i in p:
        while t < 11:
            t *= i
        s *= t/i
        print s
    print s
