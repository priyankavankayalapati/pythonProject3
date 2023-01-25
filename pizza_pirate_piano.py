l1=[]
l=["134567","pack@123e","get","parrot","pizza","","pirate","the","pet","paint","peach","test","picnic","piano"]
for i in l:

    for j in range(len(i)):
        if j==0 and i[j]=='p':
            if i[len(i)-1] in('a','e','i','o','u'):
                l1.append(i)
for i in l1:
     print(i)