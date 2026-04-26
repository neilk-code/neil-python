'''
Q3.You are developing a program
to calculate the sum of even numbers from 1 to 50,
but you want to stop the calculation if the sum exceeds 200.
Implement a program that calculates and prints the sum of even numbers,
stopping if the sum goes beyond 200.
'''
total=0
for number in range(1,50):
    total=total+number
    if total>=200:
        break
print(total)