import random

r = random.randint(0,11)

a = input("Guess the number 0~10 :")
if a == r:
    print("correct")
else:
    print("wrong") 