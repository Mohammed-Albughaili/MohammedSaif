try:
    number1 = int(input("Give me a number: "))
except ValueError:
    print("Hey I wanted a number")
    number1 = 50
else:
    print("Great Number")

number2 = 50

try:
    result = number2 / number1
except ZeroDivisionError:
    print("This is mathematical unexpected")
else:
    print(result)
finally:
    print("done")
