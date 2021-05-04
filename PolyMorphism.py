#Polymprphism means a single function works differently for diff kinds of data types.

def func(a,b,c):
    return a + b + c

a = func(6, 7, 8)
b = func("vinayak "," kisan "," dumbre ")
c = func([1,2,3],[4,5,6],[7,8,9])
print(a)
print(b)
print(c)