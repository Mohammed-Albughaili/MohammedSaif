list1 = list(range(3,15))
print(list1)
list2 = list(range(2,10))
print(list2)
list3 = list(range(5,20))
print(list3)


Ins1 = 55
Ins2 = 0
Ins3 = 44

list1.insert(8, Ins1)
print(list1)
list2.insert(5, Ins2)
print(list2)
list3.insert(-1, Ins3)
print(list3)
list1.insert(-4, 100)
print(list1)

choice1 = int(input("choose the first number in list1:"))
Insert1 = int(input("insert the first number in list1:"))

choice2 = int(input("choose the second number in list1:"))
Insert2 = int(input("insert the second number in list1:"))

choice3 = int(input("choose the third number in list1:"))
Insert3 = int(input("insert the third number in list1:"))


list1.insert(choice1,Insert1)
print(list1)
list2.insert(choice2,Insert2)
print(list2)
list3.insert(choice3,Insert3)
print(list3)
