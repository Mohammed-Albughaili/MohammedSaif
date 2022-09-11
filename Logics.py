Input1 = int(input("Number 2 of 6: "))
Input2 = int(input("Number 3 of 6: "))
Input3 = int(input("Number 4 of 6: "))
Input4 = int(input("Number 5 of 6: "))


if Input2 == Input4 and Input3 == Input4:
    print("the same number really?")

if Input3 == Input4 and Input2 == Input4:
    print("Sorry, you aren't creative, are you?")

if Input1 > Input2 and Input3 > Input4:
    print("that was true?")
if Input3+Input2 < Input4:
    print("that is false")
if Input4 >= Input3 or Input2 >= Input3:
    print(" good job")
if Input1 <= Input4 and Input2 == Input3:
    print("stabel")
