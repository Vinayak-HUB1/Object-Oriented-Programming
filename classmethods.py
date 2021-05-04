
class employee:
    raise_amount = 1.2
    no_of_emps = 0

    def __init__(self,first,last,pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = f"{first}{'.'}{last}@gmail.com"

        employee.no_of_emps+=1

    def full_name(self):
        return f"{self.first} {self.last}"

    def apply_raise(self):
        self.pay = int(self.pay*self.raise_amount)
    
    @classmethod
    def set_raise_amount(cls,amount):
        cls.raise_amount=amount
    
    @classmethod
    def from_emp_str(cls,emp_str):
        first,last,pay = emp_str.split("-")
        return cls(first,last,pay)

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday()==6:
            return False
        return True



emp_1 = employee("vinayak", "dumbre", 25000)
emp_str_1 = "vinu-dumbre-15000"

import datetime
mydate = datetime.date(2021, 6, 12)
employee.set_raise_amount(1.5)

print(emp_1.pay)
emp_1.apply_raise()
print(emp_1.pay)
print(emp_1.raise_amount)
print(employee.raise_amount)
new_emp = employee.from_emp_str(emp_str_1)
print((new_emp.pay))
print(employee.is_workday(mydate))


