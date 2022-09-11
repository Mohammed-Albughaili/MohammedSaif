#the four proteins collagen, elastin, fibrin and keratin
dictionary1 ={}
dictionary1["protein1"] = {"name": "collagen", "length": "15aa", "function": "skin protection", "location": "skin"}
dictionary1["protein2"] = {"name": "elastin", "length": "20aa", "function": "skin protection", "location": "membrane"}
dictionary1["protein3"] = {"name": "fibrin", "length": "17aa", "function": "skin protection", "location": "cell"}

print(dictionary1)
print(dictionary1["protein1"])
print(dictionary1["protein1"]["location"])

print("1: deleted")
print("2: change")
print("3: adding")

no_1 = int(input("Do you want to add the entry:?"))



print("no_1")


if no_1 == 1:
    key1= input("Which entery should be add:?")
    del dictionary1[key1]
if no_1 == 2:
    key1= input("Which entery should be add:?")
if no_1 == 3:
    key1= input("Which entery should be add:?")
print("")
print("Here we are: (proteins)")
