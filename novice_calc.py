from xgui import (App, label, button, prompt)

app: App = App.load(open("app.xml"), open("styles.style"))

total:label = app.doc.getById("total")
n1:prompt = app.doc.getById("n1")
n2:prompt = app.doc.getById("n2")
suma:button = app.doc.getById("suma")

error_text = "Valores ingresados no valido"
total_text = "Total: {T}"

def check(_n1:str, _n2:str):
    return _n1.isnumeric() and _n2.isnumeric()

@suma.events.bind("click")
def _sumar():
    n_n1 = n1.value
    n_n2 = n2.value

    if check(n_n1, n_n2):
        total.text = total_text.replace("{T}", str(int(n_n1) + int(n_n2)) )
    else:
        total.text = error_text

    app.doc.update() 

app.title("Calculadora novata")
app.size(300, 200)
app.run()