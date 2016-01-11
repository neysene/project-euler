if __name__ == '__main__':
    maxx, keep = 1, 3
    for i in xrange(2, 1000):
        num, denom, flag = 10, i, True
        a = []
        while flag:
            k = num%denom
            if k == 0:
                break
            elif k in a:
                if len(a) > maxx:
                    maxx = len(a)
                    keep = i
                break
            else:
                a.append(k)
                num = (k) * 10
    print keep

