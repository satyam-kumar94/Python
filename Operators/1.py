# Arithmetic operators
from operator import truediv
from re import A


a = 70
b = 7
print("the value of a+b is", a+b)
print("the value of a-b is", a-b)
print("the value of a*b is", a*b)
print("the value of a/b is", a/b)


# assignment operator
a = 34
a += 2
a -= 5
a *= 2
a /= 2
print(a)

# comparision operators
a = (14 <= 7)
a = (14 >= 7)
a = (14 < 7)
a = (14 > 7)
a = (14 == 7)
a = (14 != 7)
print(a)

# logical operators
bool1 = True
bool2 = False
print("the bool1 and bool2 is ", (bool1 and bool2))
print("the bool1 or bool2 is ", (bool1 or bool2))
print("the bool1 not bool2 is ", (not bool2))


# type casting
a = "2345"
a = int(a)
print(type(a))
print(a + 5)

a = 2345
a = str(a)
print(type(a))
print(a)

a = 31
a = float(a)
print(type(a))
print(a)

# input function

a = input("enter your number: ")
a = int(a)
print(type(a))
print(a)

