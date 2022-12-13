for i in range(2,21):
    f=open(f"table2.0/multiplication table of {i}.txt",'w')
    for j in range(1,11):
     f.write(f"{i}X{j}={i*j}\n" )  
    f.close()
    
      

 