def sum_over(checklist):
    result = 0
    for x in checklist:
        result += x
    return result

list1 = list(range(20))

sum1 = sum_over(list1)

print(sum1)



def reversed(checklist):
    result = 0
    for x in checklist:
        result += x
    return result
list1 = list(range(30))
rev1 = sum_over(list1)
print(rev1)
