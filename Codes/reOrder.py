a=['a','z','e','c']
b=[0, 2, 3, 1]
dict={}
c=[]
for i in range(0,len(a)):
    dict[b[i]] = a[i]
print (dict)
for i in range(0,len(a)):
    c.append(dict[i])
print (c)