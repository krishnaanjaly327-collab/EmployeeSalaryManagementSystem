from Employee import Employee

class Contract_employee(Employee):
    def calculate_salary(self,Allowance):
        Allowance = 0.05
        Total_Salary = self.salary+(self.salary*Allowance)
        print(f"Total Salary  : {Total_Salary}")