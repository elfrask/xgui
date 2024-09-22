from xgui import (Style, StyleSheets, App, COLORS)


with open("styles.json") as stylefile:

    styles= StyleSheets(stylefile.read())

with open("helloworld.xml") as AppFile:

    data = AppFile.read()


print(styles.classTags["font"])