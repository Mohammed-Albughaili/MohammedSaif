sum = 0
#with open("TestFile2.txt","r") as read_file:

    #contents = read_file.read()
#print(contents)
#print(repr(contents))

#with open("TestFile2.txt","r") as read_file3:
    #lines = read_file3.readlines()

#print(lines)

with open("TestFile2.txt","r") as read_file1:
    for line in read_file1:
    line = int(line.strip('\n'))
        sum += line
        print('The total is:',sum)
        #print(line)
        #print(repr(line))
        #print(line.strip('\n'))
