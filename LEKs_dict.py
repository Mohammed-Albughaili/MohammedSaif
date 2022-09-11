sample_dict = {}
sample_dict = {'a': 100, 'b': 200, 'c': 300}
print(sample_dict)


if "b" in sample_dict:
    print("Here we are: ")
else:
    print("This is not correct: ")


if 150 in sample_dict.values():
    print("Yes that's True ")
else:
    print("No this is False")


sample_dict = {
    'emp1': {'name': 'Jhon', 'salary': 7500},
    'emp2': {'name': 'Emma', 'salary': 8000},
    'emp3': {'name': 'Brad', 'salary': 500}
}

sample_dict["emp3"]["name"] = "Brand"
sample_dict["emp3"]["salary"] = 8500

print(sample_dict["emp3"])
