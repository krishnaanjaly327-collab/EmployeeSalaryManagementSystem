from abc import ABC,abstractmethod 

class Employee:
    def __init__(self,name,id,age,salary):
        self.name = name
        self.id = id
        self.age=age
        self.__salary=salary

    @abstractmethod
    def calculate_salary(self):
        pass
    def display_employee_details(self):
        print(f"{self.name} {self.id} {self.age} {self.__salary}")

    @property
    def salary(self):
        return self.__salary

