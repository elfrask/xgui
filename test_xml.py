import xml.etree.ElementTree as ET



App = ET.fromstring(open("helloworld.xml").read())

print(App.text)
print(App.tail)
print(App.attrib)
print(App.tag)