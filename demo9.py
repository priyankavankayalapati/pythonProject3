

class Student:

    def __init__(self,name,rollno):
        self.name = name
        self.rollno = rollno
        self.lap = self.laptop()


    def show(self):
        print(self.name,self.rollno)
        self.lap.show()

    class laptop:

        def __init__(self):
            self.brand = 'HP'
            self.cpu='i5'
            self.priya = 0

        def show(self):
            print(self.brand,self.cpu,self.priya)

s1 = Student('raji',2)
s2 = Student('Ammu',3)

s1.show()
s2.show()