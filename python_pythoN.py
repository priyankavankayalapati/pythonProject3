s=input()
a=s[0]
b=s[-1]
c=''
for i in range(1,len(s)-1):
 c=c+s[i]
print(a.upper()+c+b.upper())