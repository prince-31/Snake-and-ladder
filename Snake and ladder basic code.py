#board=[1,8:26,21:82,43:77,44:22,46:5,48:9,50:91,52:11,54:93,55:7,59:17,62:96,64:36,66:87,69:33,73:1,80:100,83:19,92:51,95:24,98:28]

import random
#jumps or fall according to ladders or snakes.
def jump_or_fall(player,n):
    if(n==8):
        print(player,'=',n)
        print('jumps via ladder from 8 to 26')
        return 26
    elif(n==21):
        print(player,'=',n)
        print('jumps via ladder from 21 to 83')
        return 82
    elif(n==43):
        print(player,'=',n)
        print('jumps via ladder from 43 to 77')
        return 77
    elif(n==44):
        print(player,'=',n)
        print("falls via snake's bite from 44 to 22")
        return 22
    elif(n==46):
        print(player,'=',n)
        print("falls via snake's bite from 46 to 5")
        return 5
    elif(n==48):
        print(player,'=',n)
        print("falls via snake's bite from 48 to 9")
        return 9
    elif(n==50):
        print(player,'=',n)
        print('jumps via ladder from 50 to 91')
        return 91
    elif(n==52):
        print(player,'=',n)
        print("falls via snake's bite from 52 to 11")
        return 11
    elif(n==54):
        print(player,'=',n)
        print('jumps via ladder from 54 to 93')
        return 93
    elif(n==55):
        print(player,'=',n)
        print("falls via snake's bite from 55 to 7")
        return 7
    elif(n==59):
        print(player,'=',n)
        print("falls via snake's bite from 59 to 17")
        return 17
    elif(n==62):
        print(player,'=',n)
        print('jumps via ladder from 62 to 96')
        return 96
    elif(n==64):
        print(player,'=',n)
        print("falls via snake's bite from 64 to 36")
        return 36
    elif(n==66):
        print(player,'=',n)
        print('jumps via ladder from 66 to 87')
        return 87
    elif(n==69):
        print(player,'=',n)
        print("falls via snake's bite from 69 to 33")
        return 33
    elif(n==73):
        print(player,'=',n)
        print("falls via snake's bite from 73 to 1")
        return 1
    elif(n==80):
        print(player,'=',n)
        print('jumps via ladder from 80 to 100')
        return 100
    elif(n==83):
        print(player,'=',n)
        print("falls via snake's bite from 83 to 19")
        return 19
    elif(n==92):
        print(player,'=',n)
        print("falls via snake's bite from 92 to 51")
        return 51
    elif(n==95):
        print(player,'=',n)
        print("falls via snake's bite from 95 to 24")
        return 24
    elif(n==98):
        print(player,'=',n)
        print("falls via snake's bite from 98 to 28")
        return 28
    else:
        return n
#ask for another round.
def another_round(p1n,p2n,pp1,pp2,r):
    print('SCORECARD after Round',r,':-')
    print(p1n,':-',pp1)
    print(p2n,':-',pp2)
    print(p1n,'you wanna play another round?')
    a=int(input('press 1 to continue or 0 to quit:-'))
    if(a==1):
        print(p2n,'you wanna play another round?')
        b=int(input('press 1 to continue or 0 to quit:-'))
        if(b==1):
            return 1
        else:
            return 0
    else:
        return 0

def play():
    p1name=input('Player 1,enter your name:-')
    p2name=input('Player 2,enter your name:-')
    turn=random.randint(1,100)
    sum1=1
    sum2=1
    r=1
    pp1=0
    pp2=0
    while(1):
        print(p1name,'=',sum1,' ',p2name,'=',sum2)
        y=2
        if(turn%2==0):
            print(p1name,'Your turn')
            p1=random.randint(1,6)
            print(p1)
            sum1=sum1+p1
            sum1=jump_or_fall(p1name,sum1)
            print(p1name,'=',sum1,' ',p2name,'=',sum2)
            if(p1==6):
                continue
        else:
            print(p2name,'Your turn')
            p2=random.randint(1,6)
            print(p2)
            sum2=sum2+p2
            sum2=jump_or_fall(p2name,sum2)
            print(p1name,'=',sum1,' ',p2name,'=',sum2)
            if(p2==6):
                continue
        #check winning conditions.
        if(sum1>=100):
            pp1=pp1+1
            print(p1name,'wins the round.')
            y=another_round(p1name,p2name,pp1,pp2,r)
        elif(sum2>=100):
            pp2=pp2+1
            print(p2name,'wins the round.')
            y=another_round(p1name,p2name,pp1,pp2,r)
        #if both wanna continue for another round,reset the sums.
        if(y==1):
            turn=random.randint(1,100)
            sum1=1
            sum2=1
            r=r+1
        #if any of them wanna quit,terminate the game by showing their result.
        elif(y==0):
            if(pp1>pp2):
                print(p1name,'won the match by the margin of [',pp1,'-',pp2,']')
            elif(pp1<pp2):
                print(p2name,'won the match by the margin of [',pp2,'-',pp1,']')
            else:
                print('Match levels at [',pp1,'-',pp2,']')
            print(p1name,',',p2name,'Thanks for playing.\nHave a nice day.')
            break
        else:
            turn=turn+1
    
play()