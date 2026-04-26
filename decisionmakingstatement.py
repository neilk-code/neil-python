# simple if
'''
age=int(input('Enter age:'))
# indentation:to create block
if age>=18:
    print('person is eligible for voting')
      print('bye')  #IndentationError: unexpected indent
print('done')

age=int(input('Enter age:'))
if age>=18:  # if block get executed only if condition true
    print('person is eligible for voting')
    print('bye')
print('done')

# if_else
age=int(input('Enter age:'))
if age>=18:  # if block get executed only if condition true
    print('person is eligible for voting')
    print('bye')
else:     # if condition is false else block executed
    print('person is NOT eligible for voting')
    print('Good bye!')
print('done')
'''

# marks>=90  grade  A    marks>=80  grade  B   marks>=70  grade  C   marks>=60  grade  D
# marks>=50  grade  E   marks<50  grade  Fail
# if_elif_else
Marks=int(input('Enter Marks:'))
if Marks>=90 and Marks<=100:
    print('Grade A')
elif Marks>=80 and Marks<90:
    print('Grade B')
elif Marks>=70 and Marks<80:
    print('Grade C')
elif Marks>=60  and Marks<70:
    print('Grade D')
elif Marks>=50  and Marks<60:
    print('Grade E')
elif Marks>=0  and Marks<50:
    print('Fail')
else:
    print('Input Error:Entre marks between 0 to100')