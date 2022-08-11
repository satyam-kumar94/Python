# grade based qustion
marks = int(input("enter your marks\n"))
if marks>=90:
    grade = "ex"
elif marks>=80:
    grade = "a"
elif marks>=70:
    grade = "b"
elif marks>=60:
    grade = "c"
elif marks>=50:
    grade = "d"
else:
    grade = "f"
print("your grade is " + grade)
