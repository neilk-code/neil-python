science = int(input("what is your science grade? "))
math = int(input("what is your math grade? "))
reading = int(input("what is your reading grade? "))
writing = int(input("what is your writing grade? "))
history = int(input("what is your history grade? "))

total=science+math+reading+writing+history
avg=total/5

if science<33 or math<33 or reading<33 or writing<33 or history<33:
    print("you have a failing grade")
elif total>=400 and not science<50 or math<50 or reading<50 or writing<50 or history<50:
    print("you have A+ grades")
elif avg>=75:
    print("you have A grades")
elif avg>=60:
    print("you have B grades")
elif avg>=50:
    print("you have C grades")
else:
    print("you are passing")