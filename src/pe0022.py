import csv

def generate():
    a = []
    with open('files/p0022_names.txt', 'rb') as f:
        reader = csv.reader(f)
        for row in reader:
            a.append(row)
    return a[0]

if __name__ == '__main__':
    s = sorted(generate())
    c, ov = 1, 0
    for i in s:
        t = 0
        for j in i:
            t += ord(j)-64
        ov += (t*c)
        c += 1
    print ov
