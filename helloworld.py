from xgui import (Style, StyleSheets, App, COLORS)


with open("styles.json") as stylefile:

    styles= StyleSheets(stylefile.read())

with open("helloworld.xml") as AppFile:

    data = AppFile.read()

import xml.etree.ElementTree as ET

xmlfile = ET.fromstring(data)


print(dir(xmlfile))