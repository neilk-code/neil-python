booking=str(input("enter booking type (online, advance, window): "))
brand=str(input("what brand computer you want? "))
if brand=="acer":
    cost=25000
elif brand=="hp":
    cost=35000
elif brand=="dell":
    cost=45000
elif brand=="asus":
    cost=60000
else:
    cost=80000
if booking=="online":
    cost=cost*0.9
elif booking=="advance":
    cost=cost*0.92
else:
    cost=cost
print("you must pay $",cost,)