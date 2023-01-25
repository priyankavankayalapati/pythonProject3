my_list=['a','b','c']
for i in my_list:
    if i!=my_list[-1]:
        print(i,'_',end='')
    else:
       print(i,end='')