# wap to check given num is prime or not
num = int(input("enter you num:"))
prime = True
for i in range(2, num):
    if(num % i == 0 and num!=2):
        prime = False
        break
if prime:
    print("this is prime")
else:
    print("this is not prime")
