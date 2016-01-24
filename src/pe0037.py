a = []
def isprime(n):
    if n == 1: return False
    if n == 2: return True
    if n == 3: return True
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

def is_truncatable(n, dec):
    if not isprime(n):
        return False
    nl, nr = n, n
    nl = nl%(10**(dec-1))
    nr = nr/10
    dec -= 1
    while dec > 0:
        if (not isprime(nr) or (not isprime(nl))) :
            return False
        dec -= 1
        nl = nl%(10**dec)
        nr = nr/10
    return True

def generate(n, dec):
    global a
    if is_truncatable(n, dec):
        a.append(n)
        #print n
    if dec < 6:
        generate(int(str(n)+"3"), dec+1)
        generate(int(str(n)+"7"), dec+1)
    if dec < 5:
        generate(int(str(n)+"1"), dec+1)
        generate(int(str(n)+"5"), dec+1)
        generate(int(str(n)+"9"), dec+1)

if __name__ == '__main__':
    generate(2, 1)
    generate(3, 1)
    generate(5, 1)
    generate(7, 1)
    print sum(a) - 2 - 3 - 5 - 7
