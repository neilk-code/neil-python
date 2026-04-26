kwh=int(input("how much KWh of electricity did you use? "))
if kwh>=1 and kwh<=100:
    bill=(kwh*10)
elif kwh>100 and kwh<=200:
    bill=1000+(kwh-100)*15
elif kwh>200 and kwh<=300:
    bill=1000+1500+(kwh-200)*20
elif kwh>300:
    bill=1000+1500+2000+(kwh-300)*25
else:
    print("that is not possible")
print("your bill is R$",bill)