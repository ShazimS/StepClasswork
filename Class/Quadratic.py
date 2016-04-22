def main():
    getValue()

def getValue():
    ValidInput=False
    while ValidInput==False:
        try:
            a=int(input("What is your value for A? "))
            b=int(input("What is your value for B? "))
            c=int(input("What is your value for C? "))
            x=int(input("What is your value for x? "))
            print("Your equation",a,"x^2+",b,"x","+",c,"=")
            quadratic=((a*(x**2))+(b*x)+c)
            print("Your answer is:", quadratic)
            ValidInput=True
        except:
            print("Please enter a numerical value,", end= "")

main()

