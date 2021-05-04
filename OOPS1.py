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

        

emp_1 = employee("vinayak", "dumbre", 25000)

print(emp_1.pay)
emp_1.apply_raise()
print(emp_1.pay)