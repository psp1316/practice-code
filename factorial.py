

fact=1
a=int(input("enter the number"))
for i in range (1,a+1):
    fact=fact*i
print(fact) 
while(fact%10==0):
    print(fact)

