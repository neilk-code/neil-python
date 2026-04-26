'''
Q1.Problem DescriptionA regular box of cupcakes holds 8 cupcakes, while a small box holds 3 cupcakes. There are
28 students in a class and a total of at least 28 cupcakes. Your job is to determine how many
cupcakes will be left over if each student gets one cupcake.

Input Specification
The input consists of two lines.
• The first line contains an integer R ≥ 0, representing the number of regular boxes.
• The second line contains an integer S ≥ 0, representing the number of small boxes.
Output Specification
Output the number of cupcakes that are left over.
Sample Input 1
2
5
Output for Sample Input 1
3
Explanation of Output for Sample Input 1
The total number of cupcakes is 2 × 8 + 5 × 3 which equals 31. Since there are 28 students,
there are 3 cupcakes left over.
Sample Input 2
2
4
Output for Sample Input 2
0
Explanation of Output for Sample Input 2
The total number of cupcakes is 2 × 8 + 4 × 3 which equals 28. Since there are 28 students,
there are no cupcakes left over.


regular=int(input("how many regular boxes of cupcakes are there? "))
if not regular>0:
    print("number must be greater than 0")
    regular=int(input("how many regular boxes of cupcakes are there? "))
small=int(input("how many small boxes are there? "))
if not small>0:
    print("number must be greater than 0")
    regular=int(input("how many small boxes are there? "))
leftovers=28-((regular*8)+(small*3))
print("there are ",leftovers," cupcakes left")
'''
'''
Question 2 – Result Processing System l
Input marks of 5 subjects.
Rules:
If any subject < 33 → Fail
If total ≥ 400 and no subject < 50 → Grade A+
If average ≥ 75 → Grade A
If average ≥ 60 → Grade B
If average ≥ 50 → Grade C
Otherwise → Pass
⚠️ Fail condition must override everything.


science=int(input("what is your science grade? "))
math=int(input("what is your math grade? "))
reading=int(input("what is your reading grade"))
writing=int(input("what is your writing grade? "))
history=int(input("what is your history grade? "))
if science<33 or math<33 or reading<33 or writing<33 or history<33:
    print("you are failing")
else:
    avg=(science+math+reading+writing+history)/5
    if (science+math+reading+writing+history)>400 and science>50 and math>50 and reading>50 and writing>50 and history>50:
        print("you have A+ grade")
    elif avg>75:
        print("you have A grade")
    elif avg>60:
        print("you have B grade")
    elif avg>50:
        print("you have C grade")
    else:
        print("you are passing")


Question3-Smart Billing System
Write a Python program that:
Inputs customer name
Inputs purchase amount
Inputs membership type (Gold, Silver, None)
Discount Rules:
Amount ≥ ₹25,000 → 30%
Amount ≥ ₹15,000 → 20%
Amount ≥ ₹5,000 → 10%
Otherwise → No discount
Extra Membership Discount:
Gold → extra 10%
Silver → extra 5%
⚠️ Condition:
Total discount cannot exceed 40%
Display:
Customer name
Total discount %
Final payable amount


name=str(input("what is your name? "))
price=float(input("how much does your order cost? "))
card=str(input("which membership are you? (gold, silver, none) "))

if price>25000:
    discount=0.7
elif price>15000:
    discount=0.8
elif price>5000:
    discount=0.9
else:
    discount=1

if card=="gold":
    discount=discount-0.1
elif card=="silver":
    discount==discount-0.05
else:
    discount=discount

print(f"{name}, you must pay ₹{price*discount:.2f}, with a discount of ₹{discount:.2f}.")


Question 4 – Advanced ATM Machine
Write a program that:
Input:
Account balance
Withdrawal amount
PIN
Conditions:
Correct PIN is 4321
If PIN incorrect → "Transaction Blocked"
Withdrawal must be multiple of 100
Withdrawal cannot exceed ₹20,000
Must maintain minimum balance ₹1,000
Display remaining balance or appropriate message.
'''