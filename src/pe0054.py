#it doesn't cover some scenarios which don't occur once.
#so it passed and i'm full of exception handling for today
#not smart but fast

from collections import Counter

def straight(a):
    if a[4] - a[3] == 1 or a[4] - a[3] == 9:
        if a[3] - a[2] == 1:
            if a[2] - a[1] == 1:
                if a[1] - a[0] == 1:
                    return True
    return False

def score(a):
    if len(Counter([a[0][2], a[1][2], a[2][2], a[3][2], a[4][2]])) == 1:
        if straight([int(a[0][:2]), int(a[1][:2]), int(a[2][:2]), int(a[3][:2]), int(a[4][:2])]):
            return 2500000000*int(a[4][:2])
        return 5000000*int(a[4][:2])
    elif straight([int(a[0][:2]), int(a[1][:2]), int(a[2][:2]), int(a[3][:2]), int(a[4][:2])]):
        return 250000*int(a[4][:2])

    x = Counter([int(a[0][:2]), int(a[1][:2]), int(a[2][:2]), int(a[3][:2]), int(a[4][:2])]).most_common(3)

    if x[0][1] == 4:
        return 100000000*x[0][0]
    elif x[0][1] == 3:
        if x[1][1] == 2:
           return 100000*x[0][0] + 5000*x[1][0]
        return 5000*x[0][0]
    elif x[0][1] == 2:
        if x[1][1] == 2:
            return 250*x[0][0] + 15*x[1][0] + x[2][0]
        if x[0][0] == int(a[4][:2]):
            return 15*x[0][0] + int(a[2][:2])
        else:
            return 15*x[0][0] + int(a[4][:2])
    
    return int(a[4][:2])

def file_to_list():
    f = open("files/p0054_poker.txt",'r')
    fd = f.read()
    f.close()
    fd = fd.replace("2","02")
    fd = fd.replace("3","03")
    fd = fd.replace("4","04")
    fd = fd.replace("5","05")
    fd = fd.replace("6","06")
    fd = fd.replace("7","07")
    fd = fd.replace("8","08")
    fd = fd.replace("9","09")
    fd = fd.replace("T","10")
    fd = fd.replace("J","11")
    fd = fd.replace("Q","12")
    fd = fd.replace("K","13")
    nd = fd.replace("A","14")
    f = open("files/p0054_poker_out.txt",'w')
    f.write(nd)
    f.close()
    
    count = 0
    with open("files/p0054_poker_out.txt") as f:
        for line in f:
            hand = line.split()
            if score(sorted(hand[:5])) > score(sorted(hand[5:])):
                count += 1
    return count

if __name__ == '__main__':
    print file_to_list()
