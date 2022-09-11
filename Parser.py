File = open("Unknown2.fasta", "r")
Lines = File.readlines()

for line in Lines:
    print(line.replace("\n",""))
    if ">" in line: print("This is a header")
else: print("Tis is a sequence")
