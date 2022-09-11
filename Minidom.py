import xml.dom.minidom as mini

# xml_string = "<Proteins><Pro_structure>1</Pro_structure><Experiments>2</Experiments></Proteins>"
# root1 = mini.parseString(xml_string)
# print(root1.firstChild.childNodes[1].firstChild.nodeValue)
#
# root2 = mini.parse("Experiments.xml")
# print(root2.firstChild)
# print(root2.firstChild.childNodes)
# print(root2.firstChild.childNodes[1].childNodes)
# print(root2.firstChild.childNodes[1].firstChild.nodeValue)

#xml_string2= "<Proteins><Pro_structure>1</Pro_structure><Pro_structure>2</Pro_structure></Pro_structure>3</Pro_structure></Proteins"
root3 = mini.parse("Experiments.xml")
list_nodes_b2 = mini.parse(root3)
#print(root3.firstChild)
list_nodes_b2= root3.getElementsByTagName("Experiments.xml")
sum2=0
for node in list_nodes_b2:
     sum2 += int(node.firstChild.nodeValue)
print(sum2)

# root2 = mini.parse("Books.xml")
# print(root2.firstChild)
# print(root2.firstChild.childNodes)
# print(root2.firstChild.childNodes[1].childNodes)
# print(root2.firstChild.childNodes[1].childNodes[1])
# print(root2.firstChild.childNodes[1].childNodes[1].firstChild)
# print(root2.firstChild.childNodes[1].childNodes[1].firstChild.nodeValue)
#
# root2 = mini.parseString(''.join([line.strip() for line in root2.toxml().splitlines()]))
# print(root2.firstChild)
# print(root2.firstChild.childNodes)
# print(root2.firstChild.childNodes[0].childNodes)
# print(root2.firstChild.childNodes[0].childNodes[0])
# print(root2.firstChild.childNodes[0].childNodes[0].firstChild)
# print(root2.firstChild.childNodes[0].childNodes[0].firstChild.nodeValue)
#
# xml_string2 = "<a><b>1</b><b>2</b><b>3</b></a>"
# root3 = mini.parseString(xml_string2)
# list_nodes_b2 = root3.getElementsByTagName("b")
# sum2=0
# for node in list_nodes_b2:
#     sum2 += int(node.firstChild.nodeValue)
# print(sum2)
#
# root4 = mini.parse("Music.xml")
