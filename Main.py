from PermenantEmployee import Permenant_employee
from ContractEmployee import Contract_employee


permenat = Permenant_employee("Maya","ID23",56,70000)
contract= Contract_employee("Chandhu","ID45",34,30000)

permenat.calculate_salary(0.2)
permenat.display_employee_details()

contract.calculate_salary(0.05)
contract.display_employee_details()