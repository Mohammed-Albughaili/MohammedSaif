S1 = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco lab ris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum"

print(S1[0:])
print("")

print(len(S1))
print("")

for i in range(len(S1)):
    print(S1[i])
print("")

Sp1 = S1.split()
print(Sp1)
print("")

Sp2 = S1.split(",")
print(Sp2)
print("")

import re
Sp3 = re.split(" |,|;",S1)
print(Sp3)
print("")


if "minim" in S1: print("This word is in your String, Genius")
if "anim" in S1: print("This word is in your String, Genius")
if "caesar" in S1: print("This word is in your String, Genius")
if "brutus" in S1: print("This word is in your String, Genius")
if "duis" in S1: print("This word is in your String, Genius")
print("")

print(S1.strip())
print("")

print(S1.replace("et","at"))
print(S1.replace("in","on"))
print(S1.replace("eu","au"))
print("")

print(S1.upper())
print("")

print(S1.lower())
print("")

Sp4 = S1.split()
print(Sp4)
print("")

Sp5 = S1.split(",")
print(Sp5)
print("")

for i in range(len(S1)):
    print(S1[i])
print("")

# S4 = S1 + S2
# S5 = S1 + S3
# S6 = S2 + S3
# print(S4)
# print(S5)
# print(S6)
# print("")
#
# I1 = 4
# S7 = "This string contains {} words"
# print(S7.format(I1))
# I2 = 3
# I3 = 567
# F1 = 49.95
# S8 = "I want {} pieces of item {} for {} dollars."
# print(S8.format(I2,I3,F1))
# S9 = "I want to pay {2} dollars for {0} pieces of item {1}."
# print(S9.format(I2,I3,F1))
# print("")
# S11 = "I want to pay {2} dollars for {0} pieces of item {1}.".format(I2, I3, F1)
# print(S11)
# S12 = f"I want to pay {F1} dollars for {I2} pieces of item {I3}."
# print(S12)
# S13 = "I want to pay %s dollars for %s pieces of item %s." % (F1, I2, I3)
# print(S13)
