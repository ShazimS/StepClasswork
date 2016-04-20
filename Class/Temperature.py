def main():
    x=GetTemperature()

def GetTemperature():
    return int(input("Enter temperature in fahrenheit"))

InputValid=True
while (InputValid==True):
    x=GetTemperature()
    print("Celsius=",(x-32)/1.8)
    print("Fahrenheit=",x)
    decision=input("Do you want to continue? y/n")
    if decision=="y":
        print("Lets go again!")
    else:
        exit()

main()