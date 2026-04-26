numbers = []

print("Enter positive integers. Enter -1 to stop.")

while True:
    
        num = int(input("Enter a number: "))
        
        if num == -1:
            break
        
        if num > 0:
            numbers.append(num)
  

# After termination
print("\nYour input is for termination. Here is the result below:")

if numbers:
    print(f"Number of positive integers is: {len(numbers)}")
    print(f"The maximum value is: {max(numbers)}")
    print(f"The minimum value is: {min(numbers)}")
    avg = sum(numbers) / len(numbers)
    print(f"The average is {avg:.2f}")
else:
    print("No positive integers were entered.")
