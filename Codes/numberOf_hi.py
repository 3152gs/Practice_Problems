'''Return the number of times that the string "hi" appears anywhere in the given string. 

count_hi('abc hi ho') → 1
count_hi('ABChi hi') → 2
count_hi('hihi') → 2 '''

a= 'ABChi hi'
count=0
for i in range(0,len(a)-1):
    if (a[i]=='h'):
        if (a[i+1]=='i'):
            count+=1
            
print (count)
