def maximum(num1,num2,num3):
    if(num1>num2 and num1>num3):
        return num1
    elif(num2>num3):
        return num2
    else:
         return num3
total=maximum(33,5,98)
print(total)
