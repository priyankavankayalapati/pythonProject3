import re
string1 = "purple*alice@@2To%%pythonprograming^^$$"
string = "Welcome to python training program"
regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
if regex.search(string1) is None:
             print("String doesn't contains Special Characters.")
else:
             print("String contains Special Characters.")
if regex.search(string) is None:
             print("String doesn't contains Special Characters.")
else:
             print("String contains Special Characters.")