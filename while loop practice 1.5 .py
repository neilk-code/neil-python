'''
Q5.task 4:

Write a program to build a simple Bank Management System
which can perform the following operations:

first admin login  if user failes enter right credentials in 3 chance
no access to sytem.
give following options after succesful login
1.Open account
2.Deposit Money
3.Withdraw Money
4.Display Account
'''
attemps=0
pw=int(1234)
while attemps<3:
    attemps=attemps+1
    attempt=int(input("password: "))
    if attempt==pw:
        break
mode=str(input("what are you doing? "))