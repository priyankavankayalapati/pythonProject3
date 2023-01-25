s=input()
print(len(s))


my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

for i in range(len(my_list)):
    if(i%2 != 0):
        print(my_list[i])


rows = 5
for i in range(0, rows + 1):
    for j in range(rows - i, 0, -1):
        print(j, end=' ')
    print()