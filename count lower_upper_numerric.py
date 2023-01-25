abc=input()
d,e,f,g=0,0,0,0
for i in abc:
    if i.islower():
        d=d+1
    elif i.isdigit():
        e=e+1
    elif i.isupper():
        f=f+1
    else:
        g=g+1
print('Numeric counts' ,e)

print('Lower counts' ,d)

print('Upper counts', f)

print('Special counts',g)