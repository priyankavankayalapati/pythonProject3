import re
s = "purple alice@google.com abcde helloab@abc.com ---@gmail.com 23@gmail.com my23@gmail.com _@gmail.com"
lst = re.findall('[a-zA-Z]\S+@\S+', s)
lst1 = re.findall('\S+@\S+', s)
print(lst1)
print(lst)