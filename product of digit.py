a=int(input("enter the number\n"))
mul=1
while(a>0):
    dig=a%10
    mul=mul*dig
    a=a//10
print("your answer is ",mul)