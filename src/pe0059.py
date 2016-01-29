#kinda lucky shot
#assume that space is the most common char

import csv
from itertools import permutations
from collections import Counter

def solver():
    x = list(csv.reader(open('files/p0059_cipher.txt')))[0]
    cntr = Counter(x).most_common(3)
    c = []
    c.append(int(cntr[0][0]) ^ 32)
    c.append(int(cntr[1][0]) ^ 32)
    c.append(int(cntr[2][0]) ^ 32)
    for i in permutations(c,3):
        s = ""
        for j in xrange(len(x)):
            p = int(x[j])^i[j%3]
            if p > 126 or p <32:
                break
            s += chr(p)
        if ' the ' in s and ' and ' in s:
            print s
            return s

if __name__ == '__main__':
    print sum([ord(i) for i in solver()])
