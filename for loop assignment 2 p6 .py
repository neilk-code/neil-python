# 6.Find sum of series: c series program
# s: 1 + x/1! + x**2 /2!+ x**3 /3!+ ... x**n/n!

sum=1
x=int(input("x: "))
r=int(input("range: "))

for i in range(1,r+1):
    fi=1
    for j in range(1,i+1):
        fi=fi*j
    sum=sum+(x**i)/fi
    print(fi,end=" ")
print(sum)