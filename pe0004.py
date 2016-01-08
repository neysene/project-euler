def is_palindrome_other(a):
    s = str(a)
    l = len(s)
    for i in xrange(l/2):
        if not (s[i:i+1] == s[l-i-1:l-i]):
            return False
    return True

def is_palindrome(a):
    return str(a) == str(a)[::-1]

if __name__ == '__main__':
    largest = 0
    for i in range(999, 100, -1):
        for j in range(999, 100, -1):
            if i*j > largest:
                if is_palindrome(i*j):
                    largest = i*j

    print largest
