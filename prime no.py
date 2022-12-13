p=int(input("enter the no\n"))
for i in range(2,p):
    if(p%i==0):
        print("its not a prime number")
        break
else:
    print("its a prime no")    
    