print("_____________________________________________________________________________________________________________________________________")


def psum(a,b):
    s=(a+b)
    #print(s)
    return s

def pmul(c,d):
    m=c*d
   #2
   # 3 print(m)
    return m


n1=int(input("Enter a number: "))
n2=int(input("Enter another number: "))

sum=psum(n1,n2)
#print(sum)

product=pmul(sum,2)
print(product)