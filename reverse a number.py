a=int(input("enter the number\n"))
rev=0
while(a>0):
   dig=a%10
   rev=rev*10+dig
   a=a//10
print('reverse is',rev) 

# num = int(input("enter a number"))

# n = num

# reverse = 0

# while n != 0:

#     rem = n % 10

#     reverse = reverse * 10 + rem

#     n = n // 10

# print("{} is reverse of {}".format(reverse,num))  