print(True*2)


str1="Python"
str2="Training"
str3="Sample"
if len(str2):
    if len(str1)<len(str2) :
        print("training is the largest of 3 strings")
    elif len(str2)<len(str3) :
        print("sample is the largest of 3 strings")
    else:
        len(str3)<len(str1)
        print("python is the largest of 3 stings")


marks =int(input("student_marks :"))

if marks < 25:
    print("the grade is F")
elif (marks >= 25) and (marks < 45):
    print("the grade is E")
elif (marks >= 45) and (marks < 50):
    print("the grade is D")
elif (marks >= 50) and (marks < 60):
    print("the grade is C")
elif (marks >= 60) and  (marks < 80):
    print("the grade is B")
else:
    print("the grade is A")
    print()



