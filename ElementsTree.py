import xml.etree.ElementTree as ET


mytree = ET.parse('Experiments.xml')
myroot = mytree.getroot()
print(myroot)
print(len(myroot))
print(myroot.tag)
print(myroot[0].tag)
print(myroot[0][1].tag)
print(myroot[0][1].text)

for x in myroot.findall('experiment'):
    title =x.find('title').text
    name = x.find('name').text
    print(title, name)
