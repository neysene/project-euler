def prime_list(n):
    sieve = [True] * (n/2)
    for i in xrange(3,int(n**0.5)+1,2):
        if sieve[i/2]:
            sieve[i*i/2::i] = [False] * ((n-i*i-1)/(2*i)+1)
    return [2*i+1 for i in xrange(1,n/2) if sieve[i]]

def conjecture():
    n = 10000
    primes = set(prime_list(n))
    for i in xrange(9, 10000, 2):
        flag = False
        if i in primes:
            continue
        else:
            bound = int((i/2)**0.5)
            for m in xrange(1, bound+1, 1):
                temp = i - 2*m*m
                if temp in primes:
                    flag = True
                    break
            if not flag:
                return i
                break
        
if __name__ == '__main__':
    print conjecture()
