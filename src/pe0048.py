#second one also works. i implemented it for C.
#But Python likes big numbers

def fast_one():
    sumof = 0
    for i in range(1, 1001):
        sumof += (i**i)%10000000000
    print sumof%10000000000

def slow_one():
    sumof, temp, elde = [0]*14, [0]*14, 0
    for i in xrange(1, 1001):
        temp[0] = 1
        for m in xrange(1,11):
            temp[m]=0
        for j in xrange(i):
            for k in xrange(10):
                temp[k] *= i
            for k in xrange(10):
                while temp[k] > 9:
                    temp[k+1] += temp[k]/10
                    temp[k] = temp[k]%10
        for j in xrange(10):
            sumof[j] += temp[j]
    for i in xrange(10):
        while sumof[i] > 9:
            sumof[i+1] += sumof[i]/10
            sumof[i] = sumof[i]%10
    print sumof[9::-1]

if __name__ == '__main__':
    fast_one()
