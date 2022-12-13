a=int(input("enter  english marks "))
b=int(input("enter  sst marks "))
c=int(input("enter  maths marks "))
d=((a+b+c)/300)*100
if(a<33 or b<33 or c<33):
    print("sorry but you are fail")
elif(d>=40 ):
    print("you are pass")
else:
    print("you are fail") 
       
print("percentage is ",d)