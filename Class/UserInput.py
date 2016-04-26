def main():
    x=getItterations()
    getNumbers(x)

#    maximumNumber()

def getItterations():
    return int(input("How many numbers do you want?"))

def getNumbers(y):
    myList=[]
    a=0
    for a in range(0,y):
        numbers=int(input("What are your numbers?"))
        myList.append(numbers)

    lengthOfList = len(myList)
    sum=0
    print("The numbers you entered were:", end=" ")
    for c in range(0,lengthOfList):
        print(myList[c], end=" ")
        sum=sum+myList[c]

    e=myList
    print("Before sort: ", e)
    for j in range(len(e)):
        i=0
        for k in range(len(e)-1):
            if e[i]>a[i+1]:
                temp=e[i]
                a[i]=a[i+1]
                a[i+1]=temp
            i=i+1
    print("After sort: ", e)

main()

'''
def maximumNumber():
    c=0
    while c in myList[0,y]:
        if c+1>c:
            print=(c)
'''
