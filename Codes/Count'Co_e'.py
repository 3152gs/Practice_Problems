'''Return the number of times that the string "code" appears anywhere in the given string, except we'll accept any letter for the 'd', so "cope" and "cooe" count. 

count_code('aaacodebbb') → 1
count_code('codexxcode') → 2
count_code('cozexxcope') → 2
'''
a = 'cozexxcope'
count=0
for i in range(0, len(a)-3):
    if (a[i]=='c' and a[i+1]=="o" and a[i+3]=='e'):
        count+=1
print (count)