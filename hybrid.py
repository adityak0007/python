class Person:
    def details(self):
        print("I am a person")

class Teacher(Person):
    def teach(self):
        print("I can teach")

class Student(Person):
    def study(self):
        print("I can study")

class Monitor(Student, Teacher):
    def duty(self):
        print("I am a class monitor and I manage duties")
        

t = Teacher()
s = Student()
m = Monitor()

t.details()
t.teach()

s.details()
s.study()

m.details()
m.teach()
m.study()
m.duty()
