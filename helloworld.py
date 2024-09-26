from xgui import (Style, StyleSheets, App, COLORS, Components, DEFAULT_COMPONENTS)


with open("styles.json") as stylefile:

    styles= StyleSheets(stylefile.read())

with open("helloworld.xml") as AppFile:

    data = AppFile.read()


app = App(DEFAULT_COMPONENTS)

dom = app.build(data, styles, 300, 200, 300, 200)
print(dom.getTreeBuild().children)