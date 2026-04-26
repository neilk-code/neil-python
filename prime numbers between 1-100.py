# task: print prime numbers between 1-100
for number in range(1,101):
    factors=0
    for i in range(1,number+1):
        if number%i==0:
            factors=factors+1
    if not factors>2:
        print(number,end=" ")