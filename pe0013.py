def file_to_list():
    with open("files/p0013_numbers.txt", "r") as f:
        l, a = [line.split() for line in f], []
        for i in xrange(100):
            t = []
            for j in xrange(13):
                t.append(int(l[i][0][j]))
            a.append(t)
    return a

if __name__ == '__main__':
    m, k, l = file_to_list(), 0, ""
    for i in xrange(12,-1,-1):
        s = k
        for j in xrange(100):
            s += m[j][i]
        l = str(s%10) + l
        k = s/10
    l = str(k) + l
    print l[:10]
