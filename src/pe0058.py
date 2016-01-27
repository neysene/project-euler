#CAUTION: around 15 sec
#some other primality tests may reduce runtime

def isprime(n):
    if n % 2 == 0: return False
    if n % 3 == 0: return False

    i = 5
    w = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += w
        w = 6 - w
    return True

if __name__ == '__main__':
    t, p, i, s = 1, 1, 0, 1
    while t/p < 10:
        i += 2
        if isprime(s+i):
            p += 1
        if isprime(s+ 2*i):
            p += 1
        if isprime(s+ 3*i):
            p += 1
        s += 4*i
        if isprime(s):
            p += 1
        t += 4
    print i+1
