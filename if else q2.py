a=int(input("enter first number"))
b=int(input("enter second number"))
c=int(input("enter third number"))
d=int(input("enter fourth number"))

if(a>d):
    f1=a
else:
    f1=d
if(b>d):
    f2=b
else:
    f2=c
if(f1>f2):
    print(f1,"is greatest")
else:
    print (f2, "is greatest")                
