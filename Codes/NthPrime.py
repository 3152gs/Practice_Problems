factcount =0
c=2
count =0
while (c>=0):
    
    factcount = 0
    for i in range (2, (c//2+1)):
        if (c % i == 0):
            factcount+=1
            break
    if factcount==0:
        count+=1
    if count == 5:
        print (c)
        break
    c+=1   
    