if __name__ == '__main__':
    result = 0

    for i in xrange(1000000):
        if str(i) == str(i)[::-1] and str(bin(i))[2:] == str(bin(i))[2:][::-1]:
            result += i
    print "Answer is", result
