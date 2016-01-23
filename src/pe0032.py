def isPandigital(stringo):
    for i in xrange(1, 10):
        if str(i) not in stringo:
            return False
    return True

if __name__ == '__main__':
    product = set()
    for i in xrange(1, 10):
        for j in range(1000, 10000):
            if((i*j)>9999):
                break
            stringo = str(i) + str(j) + str(i*j)
            if(len(stringo) != 9):
                continue
            if(isPandigital(stringo)):
                product.add(i*j)
                #print i, " * ", j, " = ", (i*j)
    for i in xrange(10, 100):
        for j in range(100, 1000):
            stringo = str(i) + str(j) + str(i*j)
            if(len(stringo) != 9):
                continue
            if(isPandigital(stringo)):
                product.add(i*j)
                #print i, " * ", j, " = ", (i*j)
    print 'Problem 32 - Answer is ', sum(product)
