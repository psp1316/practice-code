i=int(input("enter the number"))
if i<0:
    print("enter natural number")
else:
    sum=0
    while(i>0):
        sum=sum+i
        i=i-1
    print("your sum is ",sum)        