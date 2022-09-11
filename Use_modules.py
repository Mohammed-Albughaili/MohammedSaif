import random

choice1=int(input("please guss the specific number!"))
choice2= random.randrange(90)

print(choice2)

while choice1 != choice2:

    print("Good")
    if choice2 < choice1:
        print("your number is bigger")
    if choice2 > choice1:
        print("your number is smaller")
    choice1=int(input("please guss the specific number!"))
else:
    print("the end")
    choice1=int(input("please guss the specific number!"))
