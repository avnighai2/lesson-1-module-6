# should be a multiple of 4
#  either its a multiple of 400 or after divinding by hundred remainder is not equal to 0 

year = int(input("Enter the year:"))

if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print("the year is a leap year")
else:
    print("the year is not a leap year")