#i just don't wanna use recursive or dp

if __name__ == '__main__':
    count = 0

    for i in xrange(2):
        for j in xrange((200- i*200)/100 + 1):
            for k in xrange((200 - i*200 - j*100)/50 +1):
                for l in xrange((200 - i*200 - j*100 - k*50)/20 +1):
                    for m in xrange((200 - i*200 - j*100 - k*50 - l*20)/10 +1):
                        for n in xrange((200 - i*200 - j*100 - k*50 - l*20 - m*10)/5 +1):
                            for p in xrange((200 - i*200 - j*100 - k*50 - l*20 - m*10 - n*5)/2 +1):
                                count += 1
                            
    print count
