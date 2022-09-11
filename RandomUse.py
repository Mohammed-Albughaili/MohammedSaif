import random


Input1 = int(input("give me the first list?"))
Input2 = int(input("the end of the first list?"))
Input3 = int(input("the start of the first list?"))
Input4 = int(input("the end of the list2?"))
Input5 = int(input("the start of the list2?"))
Input6 = int(input("the end of the list3?"))

random_list1 = list(range(random.randint(Input1, Input2)))
random_list2 = list(range(random.randint(Input3, Input4)))
random_list3 = list(range(random.randint(Input5, Input6)))

print(random_list1)
print(random_list2)
print(random_list3)

Input7 = int(input("How many floats? "))

for x in range(Input7):
    random_float = random.random()
    print(random_float)
