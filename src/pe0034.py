#upperbound 9!*7
#this is much more efficient in C

if __name__ == '__main__':
    result, factorial = 0, [1]
    for i in xrange(1, 10):
        factorial.append(factorial[i-1] * i)

    for j in xrange(10, 2540161):
        temp, tempsum = j, 0
        while temp > 0:
            tempsum += factorial[temp%10]
            temp //= 10
        if tempsum == j:
            result += j
            #print j
    print 'Problem 34 - Answer is ', result
