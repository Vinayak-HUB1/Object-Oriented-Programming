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

class developer(employee):
     def __init__(self,first,last,pay,prog_lang):
         super().__init__(first, last, pay)
         self.prog_lang=prog_lang


class manager(employee):
    raise_amount = 2.0
    def __init__(self,first,last,pay,employees=None):
        super().__init__(first, last, pay)
        if self.employees == None:
            self.employees=[]
        else:
            self.employees=employees
    
    def add_employee(self,emp):
        if self.emp not in self.employee:
            self.employee.append(emp)

    def print_emp(self):
        if emp in self.employees:
            print(emp.full_name())

    

emp_1 = employee("vinayak", "dumbre", 25000)
dev_1 = developer("swarali", "dandwate", 100000,"python")
mgr_1 = manager("vikas", "Dandwate", 500000,[dev_1])

print(emp_1.pay)
emp_1.apply_raise()
print(emp_1.pay)
print(dev_1.pay)
print(dev_1.prog_lang)
print(mgr_1.print_emp())