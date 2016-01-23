#making prime list to a set is reduce runtime from 2.5 minutes to 25 ms

def primelist(n):
    sieve = [True] * (n/2)
    for i in xrange(3,int(n**0.5)+1,2):
        if sieve[i/2]:
            sieve[i*i/2::i] = [False] * ((n-i*i-1)/(2*i)+1)
    return [2] + [2*i+1 for i in xrange(1,n/2) if sieve[i]]

def isCircular(k, plist):
    n = k
    for i in xrange(len(str(k))):
        n = int(str(n%10) + str(n//10))
        if n not in plist:
            return False
    return True

if __name__ == '__main__':
    plist = set(primelist(10**6))
    circular = [2, 3, 5, 7]
    for i in plist:
        if isCircular(i, plist):
            circular.append(i)
    #print circular
    print 'Problem 35 - Answer is ', len(circular)
