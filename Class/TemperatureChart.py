'''
def main():
    GetTemperature()
    TemperatureF()
#    TemperatureC()
#    Chart()

def GetTemperature():
    return int(input("Input your temperature in Celsius from 0-100?"))
x=GetTemperature()

def TemperatureF():
    f=(x*1.8+32)
    print(f)

main()
'''

def main():
    for x in range(0,21):
        celsius=(x*5)
        fahrenheit=(celsius*1.8+32)
        print(celsius,"C to",fahrenheit,"F")

main()