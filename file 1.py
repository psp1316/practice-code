from cgitb import text


f=open('poem.txt','w')
f.write("twinkle twinkle little star hello demon how you are")
f=open('poem.txt','r')
text=f.read()
print(text.count("twinkle"))
f.close()