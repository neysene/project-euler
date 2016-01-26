def check_numbers(a):
    sa, b = str(a), a
    for k in xrange(5):
        b += a
        sb = str(b)
        for i in xrange(len(sb)):
            if sb[i] not in sa:
                return False
    print a
    return True

def start():
    k = 2
    while True:
        for i in xrange(10**k,(10**(k+1))/6):
            if check_numbers(i):
                return
        k += 1

if __name__ == '__main__':
    start()
