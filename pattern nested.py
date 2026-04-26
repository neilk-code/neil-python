'''
nested for  loop:
print  following pattern:
1
2  2
3  3  3
4  4  4   4
5  5  5   5  5


for i in range(1,6):   # rows
    for j in range(1,i+1):  # columns
        print(i, end='   ')
    print()

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

nested for  loop:
print  following pattern:
1   2   3   4   5
1   2   3   4
1   2   3
1   2
1

for i in range(1,6):   # rows
    for j in range(1,7-i):  # columns
        print(j, end='   ')
    print()

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
Write a program  to display the first n terms of the Fibonacci series.Fibonacci series 0 1 2 3 5 8 13 .....
hint :sum of previous 2 number is 3 rd number
Test Data :
Input number of terms to display : 10
Here is the Fibonacci series upto to 10 terms :
0 1 1 2 3 5 8 13 21 34
'''

term=int(input("how many term "))

for first in range(1,term+1):
    for second in range(1,3):
        if second%2==0:
            