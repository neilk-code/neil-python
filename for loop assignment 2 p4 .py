for i in range(2,1001):
    f=0
    for j in range(1,i+1):
        if i%j==0:
            f=f+1
    if f>2:
        print(j)