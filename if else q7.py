a=int(input("enter your english marks:"))
b=int(input("enter your sst marks:"))
c=int(input("enter your maths marks:"))
d=int(input("enter your science marks:"))
marks=(a+b+c+d)/4
print(marks)
if(marks<50):
    print("your overall grade is f")
elif(marks>=50 and marks<=60):
    print("your overall grade is d")
elif(marks>=60 and marks <=70):
    print("your overall grade is c")    
elif(marks>=70 and marks <=80):
    print("your overall grade is b")
elif(marks>=80 and marks<=90):
    print("your overall grade is a")
else:
    print("your overall grade is a+")        
