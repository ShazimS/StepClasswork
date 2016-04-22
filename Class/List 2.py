def main():
    favColor()




def favColor():
    firstList=[]
    secondList=[]
    for a in range (0,1):

        x=getname()
        firstList.append(x)

    for b in range (0,1):

        c=getcolor()
        secondList.append(c)
    print(x,"favorite color is",c)
#    main() #run infinite loop!!!!





def getname():
    return input("What is your name?")

def getcolor():
    return input("What is your fav color?")

main()