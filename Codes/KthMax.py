'''Find kth maximum '''

a= [2,3,1,76,43,5,9]
maxi = a[0]
count = 0
k = 4
for i in range (0,len(a)):
    count = 0
    for j in range(0, len(a)):
        if a[i]<a[j]:
            count+=1
    if count==k-1:
        print (a[i])