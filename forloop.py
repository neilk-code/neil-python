'''for number  in range(1,11,1):
     print(number, end='  ')
print()
for number  in range(20,41,2):
     print(number, end='  ')

print()
for number  in range(10,0,-1):
     print(number, end='  ')
print()


for number  in range(1,11): # by default  update consider +1
     print(number, end='  ')
print()

for number  in range(11): # by default start 0  and by default  update consider +1
     print(number, end='  ')
print()


# task :print number between 50-100 divisible by 2 and 3
for number in range(50,101,1):
    if number%2==0 and number%3==0:
        print(number,end=' ')
'''

number=int(input('Enter number:'))
for factor in range(1,number+1,1):
    if number%factor==0:
        print(factor)