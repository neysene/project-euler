def file_to_list():
    with open("files/p0011_numbers.txt") as textFile:
        l = [line.split() for line in textFile]
        for i in xrange(20):
            for j in xrange(20):
                l[i][j] = int(l[i][j])
    return l
if __name__ == '__main__':
    l, m = file_to_list(), 1
    for i in xrange(20):
        for j in xrange(20):
            if i<17 and j<17:
                dia = l[i][j]*l[i+1][j+1]*l[i+2][j+2]*l[i+3][j+3]
                if dia > m:
                    m = dia
            if j<17:
                ho = l[i][j]*l[i][j+1]*l[i][j+2]*l[i][j+3]
                if ho > m:
                    m = ho
            if i<17:
                ve = l[i][j]*l[i+1][j]*l[i+2][j]*l[i+3][j]
                if ve > m:
                    m = ve
            if j<17 and i>2:
                redia = l[i][j]*l[i-1][j+1]*l[i-2][j+2]*l[i-3][j+3]
                if redia > m:
                    m = redia
    print m
