for i in range(1,11):
    for j in range(1,(i*11)):
        if j%i==0:
            print(j)
    print()