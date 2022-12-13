# with open("comments.txt",'w') as f:
#     f.write('''hey bro you are nice but looking donkey
#     what a donkey you are 
#     nic looks amn
#     what a foolish donkey''')
# with open("comments.txt",'r') as f:
#     t=f.read()
#     t=t.replace("donkey","####")
# with open("comments.txt",'w') as f:
#     f.write(t)    

with open("comments.txt",'w') as f:
    f.write('''hey bro you are nice but looking donkey
    what a fuck donkey you are 
    nic looks mota
    what a foolish donkey''')
words=["donkey", "mota", "fuck",]    
with open("comments.txt",'r') as f:
    t=f.read()
for word in words:
    t=t.replace(word,"####")
    with open("comments.txt",'w') as f:
     f.write(t)    

