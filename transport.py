d=int(input("how far did you travel? "))

if d>=1 and d<=50:
    print("you will be charged R$",(8*d))
elif d>50 and d<=100:
    print("you will be charged R$",(10*d))
elif d>100:
    print("you will be charged R$",(12*d))
else:
    print("that doesn't make sense")