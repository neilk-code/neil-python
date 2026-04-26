balance=float(input("how much money do you have? "))
pin=str(input("enter PIN "))

if pin=="4321":

    withdrawal=int(input("how much would you like to withdraw? "))

    if not withdrawal%100==0:
        print("error, withdrawal must be a multiple of 100. rerun code.")

    elif not withdrawal<20000:
        print("error, withdrawal must be less than $20000. rerun code.")

    elif not (balance-withdrawal)>=1000:
        print("error, final balance must be greater than $1000. rerun code.")

    else:
        balance=balance-withdrawal
        print("your new account balance is $",balance)
        
else:
    print("wrong PIN, rerun code to access account.")