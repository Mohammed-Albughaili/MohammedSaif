#the four proteins collagen, elastin, fibrin and keratin
dictionary1 ={}
dictionary1["protein1"] = {"name": "collagen", "length": "15aa", "function": "protection", "location": "skin", "55": "good", "nice": "plasma"}
dictionary1["protein2"] = {"name": "elastin", "length": "20aa", "function": "elasticity", "location": "membrane", "76": "good", "nice": "plasma"}
dictionary1["protein3"] = {"name": "fibrin", "length": "17aa", "function": "protection", "location": "cell", "99": "sad", "nice": "plasma"}
dictionary1["protein4"] = {"name": "keratin", "length": "22aa", "function": "signalling", "location": "body", "40": "pefect", "nice": "plasma"}
dictionary1["protein5"] = {"name": "actin", "length": "20aa", "function": "transporter", "location": "cytoplasm", "34": "short", "nice": "plasma"}
dictionary1["protein6"] = {"name": "myocin", "length": "10aa", "function": "signaling", "location": "cell membrane","12": "long", "nice": "plasma"}
dictionary1["protein7"] = {"name": "gorab", "length": "11aa", "function": "transporter", "location": "golgi", "48": "deep", "nice": "plasma"}
dictionary1["protein8"] = {"name": "iga", "length": "16aa", "function": "defence", "location": "salive", "50": "bad", "nice": "plasma"}

print(dictionary1)
print(dictionary1["protein1"])
print(dictionary1["protein1"]["location"])

print("1: display")
print("2: manipulate")
print("3: adding")

choice_1 = int(input("would you like to make changes the entry:?"))



print("choice_1")


if choice_1 == 1:
    key1= input("Which entery should be add:?")
    del dictionary1[key1]
if choice_1 == 2:
    key1= input("what is the location for your protein:?")
if choice_1 == 3:
    key1= input("what is the function of your protein:?")
    key1= input("what it's size")

print("")
print("Here we are: (proteins)")
