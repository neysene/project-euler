def solution():
    for a in range(1,300):
        sa = a**2
        for b in range(a,500):
            sb = b**2
            c = 1000 - a - b
            if c**2 == sa + sb:
                return a, b, c, a*b*c

if __name__ == '__main__':
    print solution()
