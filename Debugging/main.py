#range error fix
import random


def myfunction():
    for i in range(1,21):
        if i == 20:
            print("You Got it")

# myfunction()

# index error fixing

from random import randint
dice = ["1️⃣","1️⃣","1️⃣","1️⃣","1️⃣"]
randomized = randint(0,5)
# print(dice[randomized])

# play computer

# year = int(input("Enter The Year:"))
# if year > 1980 and year < 1994:
#     print("You are millenial.")
# elif (year >= 1994):
#     print("You are Genz")

# Type error

#
#
# age = int(input("Enter You age:"))
# if age > 18:
#     print("You can drive")

unmatched = []
for number in range(1,101):
    if number % 3 == 0 and number % 5 == 0:
        print("Fizzbuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        unmatched.append(number)

print("Unmatched = ",unmatched)