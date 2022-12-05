import xml.sax
import xml.etree.ElementTree as ET
import xml.etree.ElementTree as ET
mytree = ET.parse('C:/Users/esmer/OneDrive/Desktop/Liverpool/Software Development/Week8/Python/food.xml')
myroot = mytree.getroot()
print(myroot)
print(myroot.tag)
print(myroot.attrib)
for x in myroot[0]:
     print(x.tag, x.attrib)

for x in myroot.findall('food'):
    item =x.find('item').text
    price = x.find('price').text
    print(item, price)





