import random

number = random.randint(1,100)
i=1
while i <= 3:
    a = int(input("enter the number from 1 to 100 "))
    if a < number:
        print("it is greater")
    elif a > number:
        print("it is smaller")
    else:
        print(f("you have corrected the right number {number}"))

    i=i+1
print(f"the number was {number}")