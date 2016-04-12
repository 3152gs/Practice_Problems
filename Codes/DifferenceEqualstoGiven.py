# Given an array, find a pair with the given difference.
# Example: Given an array, [5,20,3,2,50,80], find a pair from the array such that it’s difference is equal to the number given. If the number given is 78, the output should be 2 and 80.
a=[5,20,3,2,50,80]
sumlist=[]
k=30
for i in a:
    sumlist.append(k+i)
for i in sumlist:
    if i in a:
        if (i-k) in a:
            print (i, i-k)