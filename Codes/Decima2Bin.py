'''Convert integer to binary'''


a = 54
bin = []
rem=0
fin = 0
while a!=0:
    rem = a%2
    bin.append(rem)
    a = a//2
for i in range (len(bin)-1,-1,-1):
    fin = fin*10 +bin[i]
print (fin)

