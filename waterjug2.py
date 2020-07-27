
def displayRules(jug1,jug2):
    #to Dislplay commands to user or to give user instructions
    print("Enter 1 for  Fill  {}  Litre Jug".format(jug2))
    print("Enter 2 for Fill {} Litre Jug".format(jug1))
    print("Enter 3 for Transfer all the water from  {} Litre Jug to  {}  Litre Jug".format(jug2,jug1))
    print("Enter 4 for Transfer all the water from  {} Litre Jug to  {} Litre Jug".format(jug1,jug2))
    print("Enter 5 for Transfer some water from  {}  Litre Jug to {} Litre Jug until {} is full".format(jug2,jug1,jug1))
    print("Enter 6 for Transfer some water from  {} Litre Jug to {} Litre Jug until  {} full".format(jug1,jug2,jug2))
    print("Enter 7 for Empty {}  Litre Jug".format(jug1))
    print("Enter 8 for Empty  {} Litre Jug".format(jug2))
    print("Enter any else number to exit")
    ch = int(input("Enter your choice according above prefrence:"))
    return ch



def gamestart(x,y,jug1,jug2,goal):
    while (x != goal) and (y != goal):
        ch = displayRules(jug1, jug2)
        if ch==1:
            if(y<jug2):
                x=x
                y=jug2
                print(x,y)
            else:
                print("Rule cannot be applied")
                continue
        elif ch == 2:
            if (x < jug1):
                x = jug1
                y = y
                print(x, y)
            else:
                print("Rule cannot be applied")
                continue
        elif ch == 3:
            if (y > 0) or (x + y <= jug1):
                x = x + y
                y = 0
                print(x, y)
            else:
                print("Rule cannot be applied")
                continue
        elif ch == 4:
            if (x > 0) and (x + y <= jug2):
                x = 0
                y = x + y
                print(x, y)
            else:
                print("Rule cannot be applied")
                continue
        elif ch == 5:
            if (y > 0) and (x + y > jug1):

                y = y - (jug2 - x)
                x = jug1
                print(x, y)
            else:
                print("Rule cannot be applied")
                continue
        elif ch == 6:
            if (x > 0) and (x + y > jug2):
                x = x - (jug2 - y)
                y = jug2
                print(x, y)
            else:
                print("Rule cannot be applied")
                continue
        elif ch == 7:
            if (x > 0):
                x = 0
                y = y
                print(x, y)
            else:
                print("Rule cannot be applied")
                continue
        elif ch == 8:
            if (y > 0):
                x = x
                y = 0
                print(x, y)
            else:
                print("Rule cannot be applied")
                continue
        else:
            print("invalid charchter so exiting program")
            break
    return x,y


jug1 = int(input("Enter Jug 1 value"))
jug2 = int(input("Enter Jug 2 value"))
goal = int(input("Taget value"))
x=0
y=0
x,y=gamestart(x,y,jug1,jug2,goal)
print("After reaching the target value in the Game value in jug")
print(x,y)
