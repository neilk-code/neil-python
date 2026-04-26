'''
Q1.Username and password inputs with 3 attempts in Python.

To take username and password input values with 3 attempts:


Use a while loop to iterate a maximum of 3 times.

Use the input() function to take values for the username and password from the user.

If the credentials are correct, break out of the loop.
'''
i=0
username=input("username:")
password=input("password:")
while i<3:
    i=i+1
    print(i)
    attempt=input("enter password: ")
    if attempt==password:
        break
if attempt==password:
    print("granted")
else:
    print("denied")