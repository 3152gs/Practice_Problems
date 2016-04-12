a = "programmingproblem"
b = [6,5,7]
c=b[0]
new=""
d = 0
for i in range(0,len(a)):
    if (i<c):
        new+=a[i]
    if (i==c):
        new+=";" + a[i]
        d+=1
        c+=b[d]
    
            
print (new)