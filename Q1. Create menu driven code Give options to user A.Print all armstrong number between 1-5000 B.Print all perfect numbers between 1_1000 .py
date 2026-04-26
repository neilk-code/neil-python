'''
Q1.
Create menu driven code
Give options to user A.Print all armstrong number between 1-5000
B.Print all perfect numbers between 1_1000
'''
choice=input("A or B? ")

if choice=="a":
    print("All armstrong numbers between 1 and 5000:")
    for n in range(1,50001):
        sum=0
        e=n
        while(n!=0):
            r=n%10
            sum=sum+r**3
            n=n//10
        if e==sum:
            print(e)
else:
    print("All perfect numbers between 1-1000")
    for n in range(1,1001):
        f=0
        for i in range(1,n):
            if n%i==0:
                f=f+i
        if f==n:
            print(n)