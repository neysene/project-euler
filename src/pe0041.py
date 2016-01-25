def is_prime(n):
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
    
def permutation(s):
    if len(s) <= 1: 
        yield s
    else:
        for i in range(len(s)):
            for p in permutation(s[:i] + s[i+1:]):
                yield s[i] + p

if __name__ == '__main__':
    st = "7654321"
    a = list(permutation(st))
    for i in a:
        if is_prime(int(i)):
            print i
            break
