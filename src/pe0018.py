def file_to_list():
    with open("files/p0018_numbers.txt") as textFile:
        l = [line.split() for line in textFile]
        for i in xrange(15):
            for j in xrange(i+1):
                l[i][j] = int(l[i][j])
    return l
if __name__ == '__main__':
    l, m = file_to_list(), 1
    for i in xrange(13, -1, -1):
        for j in xrange(i+1):
            l[i][j] = l[i][j] + ( l[i+1][j] if l[i+1][j] > l[i+1][j+1] else l[i+1][j+1])
    print l[0][0]
