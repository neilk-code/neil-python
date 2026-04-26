number1=int(input("pick a number "))
number2=int(input("pick a second number "))

sum=0
for i in range(1,number1):
    if number1%i==0:
        sum=sum+i

if sum==number2:
    sum=0
    for i in range(1,number2):
        if number2%i==0:
            sum=sum+i
    if sum==number1:
        print(number1," and ",number2," are amicable")
    else:
        print(number1," and ",number2," are not amicable")
else:
    print(number1," and ",number2," are not amicable")