list1 = list(range(3,15))
print(list1)

Check1 = 5
Check2 = 12
Check3 = 20

if Check1 in list1:
    print("You found a number inside the list. Genius!")
else:
    print("don't know what numbers are in the list?")
if Check2 in list1:
    print("You found a number inside the list. Genius!")
else:
    print("don't know what numbers are in the list?")
if Check3 not in list1:
    print("You found a number inside the list. Genius!")
else:
    print("You found a number inside the list. Genius!")
