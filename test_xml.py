
# from typing import Any
# event = {}

# class add:

#     EVENT = ""
#     FUNCTION = None

#     def __init__(self, _event) -> None:
#         self.EVENT = _event
        
#         pass

#     def __call__(self, _func):
#         self.FUNCTION = _func

#         event[self.EVENT] = _func

#         return self

#     def exec(self, *arg, **args):

#         return self.FUNCTION(*arg, **args)


# @add("click")
# def _main():
#     print("Hello World")
#     pass

# print(event)
# print(_main)

# _main.exec()


# import xml.etree.ElementTree as ET

# with open("helloworld.xml") as a:
#     _d = a.read()
#     __d = ET.fromstring(_d)
#     print(list(__d))

import tkinter
from tkinter import(Label, Widget)

root = tkinter.Tk()

label = Label(root, text="Hola mundo")
label.pack(side="left")

print(isinstance(label, Widget))

root.geometry("100x100")
root.title("Hola mundo")
root.mainloop()

