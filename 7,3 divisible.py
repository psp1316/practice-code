number = int(input("Enter any Positive Number: "))

if((number % 3 == 0) and (number % 7 == 0)):
    print("Given Number {0} is Divisible by 3 and 7".format(number))
else:
    print("Given Number {0} is Not Divisible by 3 and 7".format(number))