import random
list1 = list(range(20))
random.shuffle(list1)
x = 0
result = 5
while x < len(list1):
     print("you didn't find the five")
     print("you ran", x * 2, "iterations until now")
     result = result * list1
     x += 1
print(result)
print(list1)
