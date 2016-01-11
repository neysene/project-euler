# i found this one with calculator
# then wrote a code for this algorithm

if __name__ == '__main__':
    a, f, n, lex = 2, [1], 999999, ""
    s = [0,1,2,3,4,5,6,7,8,9]

    for i in xrange(2,10):
        f.append(i * f[i-2])

    for j in xrange(8,-1,-1):
        if f[j] > n:
            continue
        lex += str(s[n/f[j]])
        del s[n/f[j]]
        n -= (n/f[j])*f[j]
    print lex + str(s[0])

