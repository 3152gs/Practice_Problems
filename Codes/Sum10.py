''' Find pairs in an integer array whose sum is 10'''

a=[1,2,3,4,1,5,6,9,2,3,0,10,8,7]
li = []
dict={}
for i in a:
    if (10-i) in a:
        if i not in li:
            li.extend([i,10-i])
    
print (li)