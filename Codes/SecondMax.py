
'''Find second largest element of list'''

a= [2,3,1,76,43,5,9]
max1=a[0]
max2=a[0]
b=[]
for i in range(0, len(a)):
    if not a[i]>max1:
        b.append(a[i])
    else:
        max1=a[i]
for i in range (0, len(b)):
    if b[i]>max2:
        max2=b[i]
print (max1)
print (max2)

