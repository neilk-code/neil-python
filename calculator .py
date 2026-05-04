def mult(n1,n2):
    sol=n1*n2
    print(sol)
def div(n1,n2):
    sol=n1/n2
    print(sol)
def add(n1,n2):
    sol=n1+n2
    print(sol)
def sub(n1,n2):
    sol=n1-n2
    print(sol)

n1=float(input("first number: "))
op=str(input("operation: "))
n2=float(input("second number: "))
if op=="*":
    mult(n1,n2)
elif op=="/":
    div(n1,n2)
elif op=="+":
    add(n1,n2)
elif op=="-":
    sub(n1,n2)
else:
    print("SYNTAX error")
