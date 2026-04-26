n1=float(input("how long is first side of triangle? "))
n2=float(input("how long is second side of triangle? "))
n3=float(input("how long is third side of triangle? "))

if n1+n2>n3 and n1+n3>n2 and n2+n3>n1:
  print("triangle is valid.")
else:
  print("triangle is not possible")