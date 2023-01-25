s=input()
l=''
for i in range(len(s)):
    if i in(0,1,len(s)-1,len(s)-2):
        l=l+s[i]

    else:
        pass
print(l)