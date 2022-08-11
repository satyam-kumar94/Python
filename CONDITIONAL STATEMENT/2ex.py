
# # wap to pass or fail
# sub1 = int(input("enter 1st subject marks\n"))
# sub2 = int(input("enter 2nd subject marks\n"))
# sub3 = int(input("enter 3rd subject marks\n"))
# if(sub1<33 or sub2<33 or sub3<33):
#     print("you are fail")
# elif(sub1+sub2+sub3)/3 <40:
#     print("you are fail because percentage less then 40%")
# else:
#     print("you are pass")

# q2-->> wap to check name present in the list or not

names = ["satyam","harry", "annu", "anmol", "saurabh"]
name = input("enter your name to check\n")
if name in names:
    print("your name is presnet in the list")
else:
    print("your name is not present in the list")