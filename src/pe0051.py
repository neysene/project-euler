#it was a challenging one for me.

def prime_list(n):
    sieve = [True] * (n/2)
    for i in xrange(3,int(n**0.5)+1,2):
        if sieve[i/2]:
            sieve[i*i/2::i] = [False] * ((n-i*i-1)/(2*i)+1)
    return [2] + [2*i+1 for i in xrange(1,n/2) if sieve[i]]

def count_prime(a, pset):
    count = 0
    for t in xrange(10):
        b = int(a.replace("x", str(t)))
        if b in pset:
            count += 1
    if count > 7:
        for t in xrange(10):
            b = int(a.replace("x", str(t)))
            if b in pset:
                print b
                return True
    return False

def start():
    last = ["1", "3", "7", "9"]
    spset = set(prime_list(100000)).difference(set(prime_list(10000)))
    bpset = set(prime_list(1000000)).difference(set(prime_list(100000)))
    for i in xrange(10):
        for j in xrange(10):
            if count_prime("xxx"+str(i)+str(j), spset): return None
            if count_prime("xx"+str(i)+"x"+str(j), spset): return None
            if count_prime("x"+str(i)+"xx"+str(j), spset): return None
            if count_prime(str(i)+"xxx"+str(j), spset): return None
            for k in last:
                if count_prime("xxx"+str(i)+str(j)+k, bpset): return None
                if count_prime("xx"+str(i)+"x"+str(j)+k, bpset): return None
                if count_prime("xx"+str(i)+str(j)+"x"+k, bpset): return None
                if count_prime("x"+str(i)+"xx"+str(j)+k, bpset): return None
                if count_prime("x"+str(i)+"x"+str(j)+"x"+k, bpset): return None
                if count_prime("x"+str(i)+str(j)+"xx"+k, bpset): return None
                if count_prime(str(i)+"xxx"+str(j)+k, bpset): return None
                if count_prime(str(i)+"xx"+str(j)+"x"+k, bpset): return None
                if count_prime(str(i)+"x"+str(j)+"xx"+k, bpset): return None
                if count_prime(str(i)+str(j)+"xxx"+k, bpset): return None

if __name__ == '__main__':
    start()
