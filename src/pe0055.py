if __name__ == '__main__':
    count = 0
    for i in xrange(1, 10000):
        flag = True
        k = i
        for j in xrange(50):
            k = k + int(str(k)[::-1])
            if str(k) == str(k)[::-1]:
                flag = False
                break
        if flag:
            count += 1
    print count
