from xgui import App

app = App.load(open("helloworld.xml"), open("styles.style"))

app.size(300, 200)
app.title("Hola mundo")

app.run()