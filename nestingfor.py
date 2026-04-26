# pattern program/ print output in the form of rows &columns
for i in range(1,5):   # rows
    for j in range(1,i+1):  # columns
        print('*', end='   ')
    print()

# filtered numbers in perticular range
for number in range(1,100000):
   sum=0      #imp
   for d in range(1,number):
       if number%d==0:
            sum=sum+d
   if sum==number:
           print(number,end=' ')