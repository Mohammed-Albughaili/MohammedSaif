list1 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,2,3,4,5]

for x in list1:
    print(x)
    if x > 20:
        pass
    print('this is the number')
    if x < 10:
            continue
    print('this is True')
    if x == 15:
            break

    print("that's it")

else:
    print("that is not my choice!")
