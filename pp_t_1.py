# import pandas as pd
#
# employee = pd.read_excel("C:\\Users\\priyankav\\Downloads\\Book2.xlsx")
#
# sal = pd.read_csv("C:\\Users\\priyankav\\Desktop\\practices\\ques1.csv")
# print(sal)
#
# emp_sal = pd.merge(employee,sal,on=['ID'],how='left')
#
# print(emp_sal)
#
# d = emp_sal.to_dict(orient='split')
#
# i, j = 0, 1
#
# tups = list(d.items())
#
# tups[i], tups[j] = tups[j], tups[i]wss
#
# res = dict(tups)
#
# print(res)

sal = open(r"C:\Users\priyankav\Desktop\practices\ques1.csv")


f = open("demofile.txt", "r")
print(f.read())