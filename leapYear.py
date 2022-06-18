def checkLeapYear():
    year = int(input("Enter the year you want to check for the leap year: "))
    if year%400==0:
        print(year,"is leap year")
    elif year%100==0:
        print(year,"is not leap year")
    elif year%4==0:
        print(year,"is leap year")
    else:
        print(year,"is not leap year")

if __name__ == '__main__':
    checkLeapYear()