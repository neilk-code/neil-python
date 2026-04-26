seat=str(input("what type of seat do you have? (ordinary, pavillion, upper pavillion, commentary box, VIP) "))
booking=str(input("what type of booking? (online, advance, none) "))

if seat=="ordinary":
    cost=2500
elif seat=="pavillion":
    cost=3500
elif seat=="upper pavillion":
    cost=4500
elif seat=="commentary box":
    cost=6000
else:
    cost=8000

if booking=="online":
    cost=cost*0.9
elif booking=="advance":
    cost=cost*0.92
else:
    cost=cost
print("your ticket is $",cost)