'''Sum of Consecutive elements that equal to the given value'''


a = [1,3,5,2,2,10,2]
b = 4
i = 0
sums = 0
c = []
while (i<len(a)):
    sums+=a[i]
    i+=1
    #print (sums)
    if sums == b:
        for j in range(0, i):
            c.append(a[j])
        
    elif (sums > b):
        sums=0
        a.remove(a[0])
        i = 0
        
print (c)