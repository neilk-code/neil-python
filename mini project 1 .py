'''
Task1 : Below are the steps:

Build a Number guessing game, in which the user selects a range.

Let’s say User selected a range, i.e., from A to B, where A and B belong to Integer.

Some random integer will be selected by the system and
the user has to guess that integer
in the minimum number of guesses
help:
to get random number use following module
import random
rnumber=random.randint(10,30) # will generate any 1 random number between 10-30
print(rnumber)
'''
import random

rnumber=random.randint(10,30)

guess=int(input("guess the number "))