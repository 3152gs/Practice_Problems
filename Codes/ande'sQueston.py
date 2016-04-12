li = [None, 2, None,1,None, None]
c=1
count=0
count2=0
last=0
#Case 1
if li[0]==None:
    while c>0:
        if li[c]==None:
            count+=1
        if li[c]!=None:
            break
for i in range(0, c):
    li[i]=li[c]
#Case II
for i in range (len(li)-1,-1,-1):
    if li[i]==None:
        count2+=1
        
    else:
        last=li[i]
        
        break
#Case III
for i in range (len(li)-1,len(li)-count2-1,-1):
    li[i]=last
for i in range(c, len(li)):
    if li[i]==None:
        li[i]=(li[i-1]+li[i+1])/2
print (li)