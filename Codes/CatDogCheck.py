'''Return True if the string "cat" and "dog" appear the same number of times in the given string. 

cat_dog('catdog') → True
cat_dog('catcat') → False
cat_dog('1cat1cadodog') → True'''

a = '1cat1cadodog'

dict={'cat':0,'dog':0}

for i in range(0,len(a)-2):
    if (a[i]=='c' and a[i+1]=='a' and a[i+2]=='t'):
        dict['cat']+=1
    if (a[i]=='d' and a[i+1]=='o' and a[i+2]=='g'):
        dict['dog']+=1
if (dict['cat'] == dict['dog']):
    print (True)
else:
    print (False)
