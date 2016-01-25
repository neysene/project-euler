def is_tri(n):
    if ((8*n + 1)**0.5)%2 == 1:
        return True
    return False

def is_pen(n):
    if ((24*n + 1)**0.5)%6 == 5:
        return True
    return False

def gen_hex():
    flag = True
    i = 144
    while flag:
        i += 1
        n = 2*i*i - i
        if is_pen(n) and is_tri(n):
            return n
        
if __name__ == '__main__':
    print gen_hex()
