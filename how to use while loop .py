sum=0
while True: # you can replace true with any condition
    number=int(input('Enter number:'))
    sum=sum+number
    if number==0:
        print(f'sum of entered numbers={sum}')
        break # break means to stop the loop

while True:
    option=int(input('Enter 1.addition 2.product 3.exit Choose any option:'))
    if option==3:
        break
    else:
         n1=int(input('Enter number1:'))
         n2 = int(input('Enter numbe2:'))
         if option==1:
             print(f'Addition{n1}+{n2}={n1+n2}')
         elif option == 2:
             print(f'product{n1}*{n2}={n1 * n2}')
         else:
             print('Invalid input')


number=int(input('Enter number'))
while number!=0:
    rem=number%10
    number=number//10
    print(f'number={number}rem={rem}')