# Datatype and variable:

x = 10
y = x
y = 20
print(x)  # 10
print(y)  # 20

a = [1, 2]
b = a
b.append(3)
print(a)  # [1, 2, 3]

x = 10
print(type(x))         # <class 'int'>
print(isinstance(x, int))  # True """

# Type casting
b = 333
t = float(b)
print(t)

# Typecasting
x = "10"
y = int(x)
print(y)

a = [1, 2]
b = [1, 2]
print(a == b)  # True
print(a is b)  # False"""
#== → value compare
#is → memory reference compare

name = 'Maaz Khan'
print(name)
bool = True
print(bool)