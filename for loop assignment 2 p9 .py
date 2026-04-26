starting=int(input("starting number of AP series: "))
items=int(input("how many numbers to be printed? "))
cd=int(input("input common difference: "))
total=starting
for n in range(1,items):
    starting=starting+cd
    total=total+starting
print(total)
