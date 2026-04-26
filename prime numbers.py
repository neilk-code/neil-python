number=int(input("pick a number "))

f=0
n=0

for n in range(1,number+1):
    if number%n==0 and not(n==1 or n==number):
        f=f+1

if f>0:
    print("not a prime number")
else:
    print("prime number")