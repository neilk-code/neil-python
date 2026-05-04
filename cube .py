def cube(n):
    c=n**3
    return c
def check(cb):
    if cb%3==0:
        print(cube(cb))
    else:
        print("not a multiple of 3")

n=int(input("lengths: "))
check(n)