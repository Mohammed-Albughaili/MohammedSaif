list1 = [1,2,3,4,5,5,7]
print(list1)
list2 = list(range(3,15))
print(list2)
list3 = list(range(2,20,4))
print(list3)
list4 = [8,9,10,11,12,13,14,15,16,17,18,19,20]
print(list4)
list5 =list(range(3,30,3))
print(list5)
list6 = list(range(2,10))

list3.append(list1)
print(list3)
list4.append(list2)
print(list4)

list1.extend(list5)
print(list1)
list2.extend(list6)
print(list2)
