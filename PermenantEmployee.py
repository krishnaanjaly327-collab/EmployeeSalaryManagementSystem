from Employee import Employee

class Permenant_employee(Employee):
    def calculate_salary(self,Allowance):
        Allowance = 0.2
        Total_Salary = self.salary+(self.salary*Allowance)
        print(f"Total Salary  : {Total_Salary}")

