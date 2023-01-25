s=input()
l=s.split()
c=0
for i in l:
    if l.count(i)<5:
        c=c+1
        print(c)