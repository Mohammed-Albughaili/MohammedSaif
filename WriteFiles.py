string1 = "Good Morning"
float1 = 3.5

file = open("TestFile.txt","w")
file.write("My name is Mohammed\n")
file.write("Hi every body\n")
file.write(string1)
file.write("\n")
file.write(str(float1))
file.close()

file = open("TestFile.txt","a")
file.write("Hallo World\n")
file.write("How are you?\n")
file.write("What are you doing?\n")
file.write(str(float1))
file.close()

with open("TestFile2.txt","w") as with_file:
    for i in range(11):
        print(i)
        with_file.write("This is a test Test\n")
        with_file.write(string1)
        with_file.write("\n")
        with_file.write(str(float1))
