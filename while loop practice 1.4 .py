'''
Q4. Aniket works in MNC.
His project manager asked him to
write a program to count the occurrence of different digits
in the entered pin and reject the pin if it contains any digits more than once.
'''
pin = input("Enter the PIN: ")
for digit in "1234567890":
    count = pin.count(digit)
if len(set(pin))<len(pin):
    print("PIN Rejected")
else:
    print("PIN Accepted")