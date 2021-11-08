def sumVect(v1,v2):
    return list(map((lambda x: x[0]+x[1]),zip(v1,v2)))
    
v1=[1,2,3]
v2=[11,22,33]
 
print(str(sumVect(v1,v2)))