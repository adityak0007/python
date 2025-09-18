class Employee:
    def __init__(self, name, age, salary):
        self.name = name          
        self.__age = age          
        self._salary = salary     

    
    def display(self):
        print(f"Name (public): {self.name}")
        print(f"Age (private): {self.__age}")
        print(f"Salary (protected/hybrid): {self._salary}")

   
    def get_age(self):
        return self.__age

    
    def set_age(self, age):
        if age > 0:
            self.__age = age
        else:
            print("Invalid age")


emp = Employee("xyz", 25, 50000)


print(emp.name) 


print(emp._salary)  


print(emp.get_age())  


emp.display()


emp.set_age(30)
emp.display()
