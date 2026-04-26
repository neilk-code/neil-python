#Q1: Write python code accept one number from user using input function and check whether a number is positive, negative or zero
'''
number=int(input("pick a number "))
if number>0:
  print(number," is positive")
elif number==0:
  print(number, "=0")
else:
  print(number, " is negative")


#Q2: write program check whether a number is even or odd.

number=int(input("pick a number "))
if number%2==0:
  print(number, " is even")
else:
  print(number, " is odd")
  '''

#Q3: write program to find maximum between three numbers.
number1=int(input("first number: "))
number2=int(input("second number: "))
number3=int(input("third number: "))
if number1>number2 and number1>number3:
  print(number1, " is greatest")
elif number2>number1 and number2>number3:
  print(number2, " is greatest")
elif number3>number1 and number3>number2:
  print(number3, " is greatest")
elif number1==number2 and number1>number3:
  print(number1," and ",number2," are greater")
elif number1==number3 and number1>number2:
  print(number1," and ",number3," are greater")
elif number2==number3 and number2>number1:
  print(number2," and ",number3," are greater")
else:
  print("all values are equivalent")