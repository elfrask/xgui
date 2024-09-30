from xgui import (App, button, prompt)

app: App = App.load(open("helloworld.xml"), open("styles.style"))
app.size(300, 200)
app.title("Hola mundo")

btn:button = app.doc.getById("btn")
_input:prompt = app.doc.getById("input")


@btn.events.bind("click")
def click():
    print("clickeado!")
    app.doc.update()

@_input.events.bind("change")
def on_change():
    print("Cambio!")

app.run()