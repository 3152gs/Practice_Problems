'''Store the avg of 'k' succesive items in a array'''

a= [2,3,1,76,43,5,9,8,7]
maxi = a[0]
avg = 0
k = 3
b=[]
sums=0
for i in range (0,len(a)):
    sums=sums+a[i]
    if ((i+1) % k == 0):
        avg = sums/k
        sums = 0
        b.append(avg)
print (b)