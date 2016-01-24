def isPandigital(stringo):
    for i in xrange(1, 10):
        if str(i) not in stringo:
            return False
    return True

if __name__ == '__main__':
    product = set()
    for i in xrange(1, 10000):
        j=1
        stringo = str(i*j)
        while(len(stringo) < 10):
            if(isPandigital(stringo)):
                #print i, " - ", stringo
                product.add(int(stringo))
            j = j + 1
            stringo = stringo + str(i*j)            

    print 'Problem 38 - Answer is ', max(product)
