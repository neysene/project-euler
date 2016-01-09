def calc(n):
    return ((999 - 999%n) + n)*(999/n)/2

if __name__ == '__main__':
    print calc(3) + calc(5) - calc(15)
