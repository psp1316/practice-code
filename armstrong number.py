a=int(input("enter the number\n"))
sum=0
order=len(str(a))
a1=a
while(a>0):
    dig=a%10
    sum=sum+(dig**order)
    a=a//10
if(a1==sum):
    print("its an armstrong number")
else:
    print("its not an armstrong number")        