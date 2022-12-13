#write a program to count first 5 number which is divided from 7 between 1356 to 2199
c=0
for i in range (1356,2199):
    if(i%7==0):
        print(i)
        c=c+1
    if(c==5): 
        break;   

            