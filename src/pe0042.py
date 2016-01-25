import csv

def check_value(a, t):
    total = 0
    count = len(a)
    for i in xrange(count):
        summon = 0
        c = a[i]
        times = len(c)
        for j in xrange(times):
            summon += (ord(c[j:j+1]) - 64)
        if summon in t:
            total += 1
    return total

def gen_tri():
    b = []
    for i in xrange(30):
        b.append((i*(i+1))/2)
    return b
        
def generate():
    a = []
    with open('files/p0042_words.txt', 'rb') as f:
        reader = csv.reader(f)
        for row in reader:
            a.append(row)
    return a[0]

if __name__ == '__main__':
    a = generate()
    t = gen_tri()
    print check_value(a, t)
