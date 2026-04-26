x=float(input("how much did the pizza cost? $"))
y=float(input("how much did the burger(s) cost? $"))
z=float(input("how much did the pasta cost? $"))
if x>y and x>z:
    print("you burned the most money on pizza")
elif y>x and y>z:
    print("you burned the most money on burgers")
elif z>x and z>y:
    print("you burned the most money on pasta")
else:
    print("everything costs the same amount")