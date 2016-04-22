myList=[1,-1,3]


def maximum():
    if myList[0]<myList[1]:
        print(myList[1])
    elif myList[2]>myList[1] and myList[0]:
        print(myList[2])
    else:
        print(myList[0])

maximum()