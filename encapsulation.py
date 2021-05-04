class manager:
    def __init__(self,name,pay,id):
        self.name = name
        self.pay = pay
        self.id = id

    def __str__(self):
        return str(self.name)+ " " + str(self.pay)+ " " + str(self.id)

class employee:
    def __init__(self,name,id,pay):
        self.name = name
        self.pay = pay
        self.id = id

    def __str__(self):
        return  str(self.name)+" "+ str(self.pay) +" " + str(self.id)

mgr = manager("sudhanshu", 50000, 2001)
emp = employee("vinayak", 123, 30000)


class company:
    def __init__(self,name,product):
        self.name = name
        self.product = product

    def __str__(self):
        return  str(self.name) + "  " + str(self.product)
        

com = company(mgr, emp)
print(com)

