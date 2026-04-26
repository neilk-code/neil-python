mph=int(input("how many mph were you going? "))
limit=int(input("what was the speed limit? "))
vehicle=str(input("what vehicle were you driving? "))
sz=str(input("are you in a school zone? "))
ro=str(input("is this your first offense? "))

over=mph-limit

if mph<=limit:
    print("no charges")
else:
    if over<10:
        fine=500
    elif over>10 and over<=20:
        fine=1500
    else:
        fine=5000
    
    if sz=="yes":
        fine=fine*2
    if ro=="no":
        fine=fine*1.5
    if vehicle=="truck":
        fine=fine+1000

    if mph>(limit*2):
        print("license suspended; ",vehicle," was going at twice the speed limit (",limit," mph )")
    else:
        print("your fine is R$",fine)