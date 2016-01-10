## tried not to eat up memory with a very big integer

if __name__ == '__main__':
    a, h, e = [1], 1, 0
    for i in xrange(2,100):
        t = 0
        while h > t:
            a[t] = (a[t] * i) + e
            e = 0
            if a[t] > 9:
                e = a[t]/10
                a[t] = a[t]%10
            t += 1
            if h==t and e>0:
                h += 1
                a.append(0)
    print sum(a)
