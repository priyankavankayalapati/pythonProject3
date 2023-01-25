

# file handling python
# 1) writing data to the file
# 2) reading data from the file
# 3) appending data to the file

# reading - r
# write - w
# append - a
# reading and writing - r+

# f = open ('my_file.txt','a')
#
# f.write('\nHello !')
#
#
# print('data is saved to file succeccfully!')
# f.close()
#
# try:
#     f=open('my_file.txt','r')
#     print(f.read())
# except:
#     print("file name does not exist")





# f=open(r'C:\Users\priyankav\Desktop\priya.txt','w')
# content=f.write('this is write')
# print(content)
# f.close()
# f=open(r'C:\Users\priyankav\Desktop\priya.txt','r')
# content=f.read()
# print(content)
# f.close()


f=open(r'C:\Users\priyankav\Desktop\priya.txt','r')
content=f.read()
print(content)
f.close()


