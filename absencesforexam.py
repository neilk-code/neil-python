absences=int(input("how many school days have you missed? "))
days=int(input("how many days of school have there been? "))
here=days-absences

if here/days>=0.75:
  print("since you attended more than 75% of school days, you may take the exam.")
else:
  print("you missed more than 25% of the year, can't take the exam.")