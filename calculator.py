no1=float(input("first number: "))
op=input("operation: ")
no2=float(input("second number: "))

if op=="*":
    print(no1*no2)
elif op=="/":
    print(no1/no2)
elif op=="+":
    print(no1+no2)
elif op=="-":
    print(no1-no2)
elif op=="//":
    print(no1//no2)
else:
    print("that's not an operator, use the symbol instead of the word.")