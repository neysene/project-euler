def find_num(finish, incr, power, i, startlist):
    start = startlist[power]
    num = 10**i
    mode = (num-start)%incr
    if mode == 0:
        mynum = ((num-start)/incr)+(10**(incr-1)) - 1
        return int(str(mynum)[-1:])
    else:
        mynum = ((num-start)/incr)+(10**(incr-1))
        return int(str(mynum)[mode-1:mode])

if __name__ == '__main__':
    a = []
    temp = 0
    start = [0]
    for k in xrange(7):
        temp += (9 * (10**k))*(k+1)
        start.append(temp)
    for i in xrange(7):
        k = 10**i
        temp, power = 0, -1
        while temp < 10**i:
            power += 1
            temp += (9*(10**power))*(power+1)
        a.append(find_num(temp, power+1, power, i, start))
    #print a
    print "The answer is", reduce(lambda x, y: x*y, a)
