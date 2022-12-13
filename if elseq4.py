comment=input("enter your comment: ")
if("fuck off"in comment):
    spam = True
else:
    spam = False
if(spam):
    print("its spam")
else:
    print("its a normal comment")    