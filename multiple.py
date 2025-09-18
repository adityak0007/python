
class Father:
    def skill1(self):
        print("Father's skill: Driving")

class Mother:
    def skill2(self):
        print("Mother's skill: Cooking")

class Child(Father, Mother):
    def skill3(self):
        print("Child's skill: Painting")


c = Child()
c.skill1()   
c.skill2()   
c.skill3()  
