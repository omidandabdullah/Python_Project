import random

number = random.randint(1,100)

while True:
    num = int(input("Guse a number between 1 and 100 : "))
    if num > number:
        print("Your guse is haghier than this...")
    elif num < number:
        print("Your guse is lower than this...")
    else:
        print("Congraluation you guse the right number")




