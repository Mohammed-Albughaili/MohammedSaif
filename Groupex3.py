#User is asked to input numbers as range input for making lists

choice1 = int(input("\nGive range for a first list starting default at 0? "))
choice2 = int(input("\nYour second list starts with number? "))
choice3 = int(input("\nAnd ends with?"))
choice4 = int(input("\nYour third list starts with? "))
choice5 = int(input("\nAnd ends with?"))
choice6 = int(input("\nAnd uses increments of?"))

#User input is used for creating 3 differrent lists.

list1 = list(range(choice1))
list2 = list(range(choice2, choice3))
list3 = list(range(choice4, choice5, choice6))


#Output lists that the user specified

print("")
print("Here are your lists")
print("")
print(list1)
print("")
print(list2)
print("")
print(list3)
print("")

#User is asked how he wants to modify the 3 lists.

choice7 = int(input("\nType in 1 for reversing all lists now or type 0 for next "))
choice8 = int(input("\nType in 2 for sorting all lists now or 0 for exit"))

if choice7 == 1:
    list1.reverse()
    list2.reverse()
    list3.reverse()
    print(list1)
    print(list2)
    print(list3)

elif choice7 == 0:
    print("You dont want to reverse")


if choice8 == 2:
    list1.sort()
    list2.sort()
    list3.sort()
    print("")
    print(list1)
    print(list2)
    print(list3)

elif choice8 == 0:
    print("")
    print("You dont want to sort")


else:
    print("")
    print("Wrong selection number. Try again")
    print("")
    
