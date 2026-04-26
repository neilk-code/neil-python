seatclass=str(input("what class seat did you book? "))
weight=float(input("how many kg does your luggage weigh? "))
IorD=str(input("are you flying international or domestic? "))
ff=str(input("are you a frequent flyer? "))

if seatclass=="economy":
    if weight<=15:
        extrakg=0
    else:
        extrakg=weight-15
elif seatclass=="business":
    if weight<=25:
        extrakg=0
    else:
        extrakg=weight-25
elif seatclass=="first":
    if weight<=40:
        extrakg=0
    else:
        extrakg=weight-40

if ff=="yes":
    extrakg=extrakg-5

if IorD=="international":
    cost=extrakg*1000
else:
    cost=extrakg*500

if extrakg>20:
    cost=cost*1.2

if weight>60:
    print("you are not allowed on the flight.")
else:
    print("you must pay R$",cost," extra for your luggage")