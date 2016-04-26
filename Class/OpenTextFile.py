f=open("C:/Users/Student_12/Desktop/test.txt","r")
myList=[]
for line in f:
    myList.append(line)
b=len(myList)
for a in range(0,b):
    print(myList[a])