#looks messy but fast

def prime_list(n):
    sieve = [True] * (n/2)
    for i in xrange(3,int(n**0.5)+1,2):
        if sieve[i/2]:
            sieve[i*i/2::i] = [False] * ((n-i*i-1)/(2*i)+1)
    return [2*i+1 for i in xrange(500,n/2) if sieve[i]]

def sub_zeros():
    pl = prime_list(10000)
    al = []
    for i in pl:
        if "0" not in str(i):
            al.append(str(i))
    return al

def permutation(s):
    if len(s) <= 1: 
        yield s
    else:
        for i in range(len(s)):
            for p in permutation(s[:i] + s[i+1:]):
                yield s[i] + p

def check_incr(se):
    rn = len(se)
    
    for i in se:
        for j in se:
            if i > j:
                if (i-j) + i in se:
                    if j == 1487:
                        return False
                    else:
                        print str(j) +  str(i) + str((i-j) + i)
                        return True
            elif j > i:
                if (j-i) + j in se:
                    if i == 1487:
                        return False
                    else:
                        print str(i) + str(j) + str((j-i) + j)
                        return True
    return False

def main():
    
    al = sub_zeros()

    for i in al:
        temp = set()
        pe = list(permutation(i))
        for j in pe:
            if j in al:
                temp.add(int(j))
        if len(temp) > 3:
            if check_incr(temp):
                return True
    return False

if __name__ == '__main__':
    main()
