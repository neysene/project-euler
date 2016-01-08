def primelist(n):
    sieve = [True] * (n/2)
    for i in xrange(3,int(n**0.5)+1,2):
        if sieve[i/2]:
            sieve[i*i/2::i] = [False] * ((n-i*i-1)/(2*i)+1)
    return [2] + [2*i+1 for i in xrange(1,n/2) if sieve[i]]

if __name__ == '__main__':
    n, i, m = 600851475143, 0, 1
    p = primelist(20000)
    while p[i] <= n:
        if n%p[i] == 0:
            n /= p[i]
            m = p[i]
        else:
            i += 1
    print m
