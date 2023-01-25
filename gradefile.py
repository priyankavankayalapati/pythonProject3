def read_grades(gradefile):

    line=gradefile.readline()

    while line != '\n':

        line=gradefile.readline()

    grade_to_ids={}

    line=gradefile.readline()

    while line != '':

        student_id=line[:4]

        grade=line[4:].strip()

        if grade not in grade_to_ids:

            grade_to_ids[grade]=[student_id]

        else:

            grade_to_ids[grade].append(student_id)

        line=gradefile.readline()

    print(grade_to_ids)

read_grades(open("C:\\Users\\priyankav\\Downloads\\gradefile.txt"))


