n=0
for n in range(1,51):
    if n%3==0 and n%5==0:
        print("fizzbuzz")
    elif n%3==0 and not n%5==0:
        print("fizz")
    elif (not n%3==0) and n%5==0:
        print("buzz")