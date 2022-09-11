number1 = int(input("Number1: "))
number2 = int(input("Number2: "))
number3 = int(input("Number3: "))
number4 = int(input("Number4: "))
number5 = int(input("Number5: "))
number6 = int(input("Number6: "))

print("Choose 1 for Multiplican")
print("Choose 2 for Division")
print("Choose 3 for Substraction")
print("Choose 4 for Addition")


choice = int(input("What operation do you want to run? "))

if choice == 1:
    result1 = number1 * number4
    print("The additional result also acceptable")
elif choice == 2:
    result2 = number6 / number2
    print("What we suspected")
elif choice == 3:
    result3 = number5 - number2
    print("that is strange")
elif choice == 4:
    result4 = number4 + number2
    print("that is true")

else:
    print("Wrong choice")
