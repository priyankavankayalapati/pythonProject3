from abc import ABC, abstractmethod

class Computer(ABC):
    @abstractmethod
    def process(self):
        pass

class Laptop(Computer):
    def process(self):
        print("its running")

class whiteboard(Computer):
    def write(self):
        print("its writing")

class Programmer:
    def work(self,com):
        print("solving bugs")
        com.process()

com1 = Laptop()
com2 = Laptop()

prog1 = Programmer()
prog1.work(com2)


com1 = Laptop()

com1.process()