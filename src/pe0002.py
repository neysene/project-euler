if __name__ == '__main__':
    j, k, c = 1, 1, 0
    while k < 4000000:
        c += j+k
        j, k = (2*k)+j, (3*k)+(2*j)
    print c
