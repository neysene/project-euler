#bounds can be shorten with some logaritmic proof

def prime_list(n):
    sieve = [True] * (n/2)
    for i in xrange(3,int(n**0.5)+1,2):
        if sieve[i/2]:
            sieve[i*i/2::i] = [False] * ((n-i*i-1)/(2*i)+1)
    return [2] + [2*i+1 for i in xrange(1,n/2) if sieve[i]]


if __name__ == '__main__':
    pl = prime_list(1000000)
    plset = set(pl)
    su = [2]
    temp = 21
    lo = 0
    
    for i in xrange(1, len(pl)):
        su.append(pl[i] + su[i-1])
        
    for j in xrange(50000):
        for k in xrange(temp+j, 50000):
            if su[k]-su[j] < 1000000:
                if su[k]-su[j] in plset:
                    if (k-j) > temp:
                        lo = su[k]-su[j]
                        temp = k-j
            else:
                break
    print lo, temp
