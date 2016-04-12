'''Print the first non repeating character in string'''


a = "aaaadgggee"
dict = {}
for i in range (0, len(a)):
    if not a[i] in dict:
        dict[a[i]] = 1
    else:
        dict[a[i]]+=1
for x in a:
    if dict[x] == 1:
        print (x)
        break
