# find the gretest in a 4 num enterd by the user
num1 = int(input("enter nnm 1: "))
num2 = int(input("enter nnm 2: "))
num3 = int(input("enter nnm 3: "))
num4 = int(input("enter nnm 4: "))
if(num1>num4):
    f1  = num1
else:
    f1 = num4

if(num2>num3):
    f2 = num2
else:
    f2  = num3
if(f1>f2):
    print(str(f1) + "is gretest")
else:
    print(str(f2) + "is gretest")