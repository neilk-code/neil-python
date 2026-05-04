def bill(cost,tip):
    total=cost+tip
    print(f"your total is {total}")

cost=float(input("cost of meal "))
tip=float(input("tip the waiter "))

bill(cost,tip)