from ._class import (COLORS, rgba, Vector2)
from ._window import (DOM, App)
import termcolor
import tkinter
import os
import xml.etree.ElementTree as ET

os.system("color")

class Style:

    CLASSNAME = ""

    size: Vector2 = Vector2()
    position: Vector2 = Vector2()
    
    positionMode: str = "relative"
    backgroundColor: rgba = COLORS.WHITE

    fontFamily: str = "Arial"
    fontSize: int = 12
    fontColor: rgba = COLORS.BLACK

    hAlign = "start"
    vAlign = "start"

    def __init__(self, data={}, classname=""):

        self.CLASSNAME = classname
        self.set(data)

        pass

    def set(self, data={}):

        for i in data:

            pre_caption = i.title().split("-")
            pre_caption[0] = str(pre_caption[0]).lower()
            caption = "".join(pre_caption)

            if hasattr(self, caption):

                type_node = getattr(self, caption).__class__
                value = data[i]

                # if type_node in [str, int, float, list, tuple, set, bool, dict]:
                if type_node == value.__class__:    
                    
                    setattr(self, caption, value)

                    pass
                elif hasattr(type_node, "parse"):
                    try:
                        
                        setattr(self, caption, 
                            type_node.parse(value)
                        )
                    except Exception as err:
                        print(termcolor.colored(f"WARNING: the value of attribute '{i}' of the class '{self.CLASSNAME}' it is not valid", "yellow"))
                        pass

                    pass
                else:
                    print(termcolor.colored(f"WARNING: the value of attribute '{i}' of class '{self.CLASSNAME}' it is not valid", "yellow"))

                    pass

                pass
            else:
                print(termcolor.colored(f"WARNING: the attribute '{i}' of the class '{self.CLASSNAME}' is not a style attribute", "yellow"))
                pass


        pass
    def __repr__(self) -> str:
        return f"Style: (name: {self.CLASSNAME})"

    pass    

class StyleSheets:

    classTags = {
        
    }

    def __init__(self, data={}) -> None:

        if isinstance(data, str):
            data = eval(data, {
                "rgba": rgba,
                "Vector2": Vector2
            })
            pass
            
        for i in data:

            self.classTags[i] = Style(data[i], i)

            pass

        pass

    def getClass(self, classname:str):

        return self.classTags.get(classname, {})

    def __repr__(self) -> str:

        return f"StyleSheets: ({ ', '.join(list(self.classTags)) })"

    pass



class Event:
    __EVENTS:dict = {}
    __ELEMENT = None

    def __gen_add(_eventName):

        def _generated(self, *arg, **args):
            
            for i in self.__EVENTS.get(_eventName, []):
                i(*arg, **args)

        return _generated

    def __init__(self, _element) -> None:
        self.__ELEMENT = _element

        pass

    def bind(self, _event: str):

        def _bind(_func):

            self.__EVENTS[_event] = self.__EVENTS.get(_event, [])
            self.__EVENTS[_event].append(_func)

            pass


        return _bind
    
    onClick = __gen_add("click")

    pass

class Element:

    tagName = "frame"
    params = {}
    parent = None
    children = []
    id: str|None = None
    style: Style
    innerText:str = ""
    events:Event
    rootDOM: DOM
    classname = ""
    __instance_element: tkinter.Widget = None
    __MASTER: tkinter.Tk



    def __init__(self, params:dict={}, parent=None, _MASTER:tkinter.Tk = None, _DOM: DOM = None):
        
        self.params = params
        self.id = params.get("id", None)
        self.classname = params.get("class", "")
        self.events = Event(self)
        self.__MASTER = _MASTER
        self.rootDOM = _DOM
        # self.children = children
        self.__on_create()

        pass
    def __ready(self):

        pass
    def setParent(self, parent):

        self.parent = parent    
    def addChild(self, child):

        self.children.append(child)
    def render(self, _Position: Vector2 = Vector2(), _Size: Vector2 = Vector2(), **_rest):

        for i in self.children:

            child: Element = i
            child.render(_Position + self.style.position, _Size + self.style.size, **_rest)
            

        return []
    def __repr__(self) -> str:

        _params = ""

        for i in self.params:

            _params += _params + f" {i}='{self.params[i]}'"
            pass

        return f"<{self.tagName} {_params}> ... </{self.tagName}>"
    
    
    pass