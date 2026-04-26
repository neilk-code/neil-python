'''
Q1  Write a program to display sum of odd numbers and even numbers
that fall between 12 and 37(including both numbers).
'''
es=0
os=0
for number in range (12,38):
    if number%2==0:
        es=number+es
    else:
        os=number+os
print("even sum: ",es)
print("odd sum: ",os)