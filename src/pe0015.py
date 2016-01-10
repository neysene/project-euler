## There should be 20 downs and 20 rights in total of 40 moves.
## So the answer is c(40, 20)

def calc_comb(n, d):
    s, t = 1, n
    for i in xrange(n, d, -1):
        s *= t
        t -= 1
    for j in xrange(d, 1, -1):
        s /= t
        t -= 1
    return s

if __name__ == '__main__':
    print calc_comb(40, 20)
