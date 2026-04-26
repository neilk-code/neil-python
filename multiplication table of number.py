table=int(input("which multiplication table do you choose? "))
n=0
for n in range((table*1),(table*10+1)):
    if n%table==0:
        print(n)