number=int(input("pick a number "))
sum=0

if number>0:
    for i in range(1,number):
        if number%i==0:
            sum=sum+i
if sum==number:
    print(number," is a perfect number")
else:
    print(number," is not a perfect number")