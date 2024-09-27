from xgui import (Style, StyleSheets, App, COLORS, Components, DEFAULT_COMPONENTS)


with open("styles.json") as stylefile:

    styles= StyleSheets(stylefile.read())

with open("helloworld.xml") as AppFile:

    data = AppFile.read()


app = App(DEFAULT_COMPONENTS)

dom = app.build(data, styles, 300, 200, 300, 200)

# print(dom.styleSheets)
# print(dom.styleSheets.classTags)
# print(dom.getTreeBuild().children[0].children)
# print(dom)
# print(App)

print("yes!")

app.size(300, 300)
app.title("Hola mundo")
app.run()