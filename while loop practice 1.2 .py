'''
Q2.Write a program that asks the user to enter positive integers in order to process
Count to total number, maximum, minimu2m, and average of numbers entered
terminate the process if user entered -1.
Sample Output:
Your input is for termination. Here is the result below:
Input: 1,34,-67,78,-32,-1
Number of positive integers is: 3
The maximum value is: 78
The minimum value is: 3
The average is 6.00
'''
numbers = []
e=0
while True:
    e=int(input("enter number "))
   # numbers=[numbers,e]
    if e==-1:
        break
    if e > 0:
        numbers.append(e)

print(f"the greatest value is {max(numbers)}")
print(f"the smallest value is {min(numbers)}")
print(f"the average is {sum(numbers)/len(numbers)}")


