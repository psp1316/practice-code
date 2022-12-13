a=int(input("enter any number\n"))
rev=0
a1=a
while(a>0):
    dig=a%10
    rev=rev*10+dig
    a=a//10
if(rev==a1):
    print("its a palindrome number\n")
else:
    print("sorry buddy")    