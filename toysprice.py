
type=int(input("what type of toy are you ordering? (1, 2, 3) "))
value=int(input("what is the value of your toy? "))

if type==1 and value>1000:
  print("you have to pay R$",(0.9*value)," with a 10% discount")
elif type==1 and value<=1000:
  print("you have to pay R$",value)
elif type==2 and value>100:
  print("you have to pay R$",(0.95*value)," with a 5% discount")
elif type==2 and value<=100:
  print("you have to pay R$",value)
elif type==3 and value>500:
  print("you have to pay R$",(0.9*value)," with a 10% discount")
elif type==3 and value<=500:
  print("you have to pay R$",value)