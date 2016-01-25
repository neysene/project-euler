def prime_list(n):
    sieve = [True] * (n/2)
    for i in xrange(3,int(n**0.5)+1,2):
        if sieve[i/2]:
            sieve[i*i/2::i] = [False] * ((n-i*i-1)/(2*i)+1)
    return [2] + [2*i+1 for i in xrange(1,n/2) if sieve[i]]

pl = prime_list(140000)
pset = set(pl)

def prime_factors(n):
    i, a = 0, set()
    while n>1:
        if n in pset:
            a.add(n)
            return len(a)
        elif n%pl[i] == 0:
            a.add(pl[i])
            while n%pl[i] == 0:
                n //= pl[i]
        i += 1
    return len(a)

def pe47():
    pf = [0,0,0]
    for i in xrange(3,500000):
        pf.append(prime_factors(i))
        if 4 == pf[i] == pf[i-1] == pf[i-2] == pf[i-3]:
            return i-3
    return "olmadi"
        
if __name__ == '__main__':
    print pe47()
