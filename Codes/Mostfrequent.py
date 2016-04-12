'''Find the most frequent integer in an array'''

a = [1,2,75,2,78,9,1,75,9,6,9,1,75,75]
dict={}

for i in a:
    if i not in dict:
        dict[i]=1
    else:
        dict[i]+=1
max = dict[a[0]]
for keys in dict:
    if (dict[keys]>max):
       max = keys
print (max)
