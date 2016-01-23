from __future__ import division

def goget():
    num, denom, count = 1, 1, 0
    for i in range(1, 10):
        for j in range(i+1, 10):
            for k in range(1, 10):
                if(i/j == ((i*10 + k)/(k*10 + j))):
                    num = num*i
                    denom= denom*j
                    count += 1
                    #print "bb--", i, " ", j, " ", k
                    if count == 4:
                        return denom/num

if __name__ == '__main__':
    print 'Problem 33 - Answer is ', goget()
