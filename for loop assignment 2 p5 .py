# 5.Find sum of series: 1 + x + x**2 + x**3 + ... x**n

x=int(input("x "))
r=int(input("range "))
sum=1
for i in range(1,r+1):
    sum=sum+(x**i)
print(sum)