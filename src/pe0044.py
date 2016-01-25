def pentagon():
    ps = set()
    i = 0
    while True:
        i += 1
        p = (3*i*i - i) / 2
        ps.add(p)
        for n in ps:
            if p-n in ps and p-2*n in ps:
                return p-2*n

if __name__ == '__main__':
    print pentagon()
