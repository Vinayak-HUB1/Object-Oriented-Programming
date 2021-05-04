class employee:
    raise_amount = 1.2
    no_of_emps = 0

    def __init__(self,first,last,pay):
        self._first = first
        self._last = last
        self._pay = pay
        self.__email = f"{first}{'.'}{last}@gmail.com"

ramesh = employee("Ramesh", "Bhosale", 15000)

print(ramesh._last)
print(ramesh.__dict__)
print(ramesh._employee__email)