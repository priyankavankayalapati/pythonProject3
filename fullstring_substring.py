s = 'abcbabc'
sb = 'bab'
c= 0
l= len(sb)
for i in range(len(s)):
    if s[i:i+l] == sb:
        c=c+1
print(c)