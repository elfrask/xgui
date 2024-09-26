from ._class import (COLORS, rgba, Vector2, clamp)
import importlib
import termcolor
import tkinter
import os
import xml.etree.ElementTree as ET

os.system("color")

__list_properties = {
    "size":"size",
    "position":"position",
    "positionMode":"position-mode",
    "backgroundColor": "background-color",
    "fontFamily": "font-family",
    "fontSize": "font-size",
    "fontColor": "font-color",
    "borderColor":"border-color",
    "borderWidth":"border-width",
    "vAlign":"v-align",
    "hAlign":"h-align",
    
}

class Style:

    CLASSNAME = ""
    __dict_style = {}
    

    size: Vector2 = Vector2()
    position: Vector2 = Vector2()
    
    positionMode: str = "relative"
    backgroundColor: rgba = COLORS.WHITE

    fontFamily: str = "Arial"
    fontSize: int = 12
    fontColor: rgba = COLORS.BLACK

    borderColor: rgba = COLORS.BLACK
    borderWidth: int = 0

    hAlign = "start"
    vAlign = "start"

    def __init__(self, data={}, classname=""):

        self.CLASSNAME = classname
        self.set(data, True)

        pass

    def set(self, data={}, __show_logs: bool = False):

        show_logs = __show_logs

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

                        self.__dict_style[caption] = value
                    except Exception as err:
                        if show_logs:
                            print(termcolor.colored(f"WARNING: the value of attribute '{i}' of the class '{self.CLASSNAME}' it is not valid", "yellow"))
                        pass

                    pass
                else:
                    if show_logs:
                        print(termcolor.colored(f"WARNING: the value of attribute '{i}' of class '{self.CLASSNAME}' it is not valid", "yellow"))

                    pass

                pass
            else:
                if show_logs:
                    print(termcolor.colored(f"WARNING: the attribute '{i}' of the class '{self.CLASSNAME}' is not a style attribute", "yellow"))
                pass


        pass
    def __repr__(self) -> str:
        return f"Style: (name: {self.CLASSNAME})"

    def getObject(self):

        _out = {}


        return self.__dict_style

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

    def getClass(self, classname:str) -> Style:

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
    onChange = __gen_add("change")

    pass


# importlib.import_module("./_window.py", ".")

class Element:

    tagName = "frame"
    params = {}
    parent = None
    children = []
    id: str|None = None
    style: Style
    innerText:str = ""
    events:Event
    # rootDOM: DOM
    rootDOM:object = None
    classname = ""
    __instance_control: tkinter.Widget = None
    __MASTER: tkinter.Tk



    def __init__(self, params:dict={}, parent=None, _MASTER:tkinter.Tk = None, _DOM = None):
        
        self.params = params
        self.id = params.get("id", None)
        self.classname = params.get("class", "")
        self.events = Event(self)
        self.__MASTER = _MASTER
        self.rootDOM = _DOM

        if isinstance(_DOM, DOM):
            self.style = parse_class_style(self.classname, self.rootDOM.styleSheets)

        # self.children = children
        self.__ready()

        pass
    def __ready(self):

        pass
    def __to_render(self, _Widget: tkinter.Widget):

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

        _c_params = list(self.params)

        for i in _c_params:

            _params += f" {i}='{self.params[i]}'"
            pass
        
        # print(_c_params)
        return f"<{self.tagName} {_params}> ... </{self.tagName}>"
    
    
    pass



def parse_class_style(class_style: str, _SS:StyleSheets) -> Style:
    # _SS: StyleSheets = _SS

    _class = class_style.split(" ")
    _out = Style()
    for i in _class:
        if not i in ["", "\t", "\n", "\r"]:
            _out.set(_SS.getClass(i).getObject())

    return _out

from ._window import (DOM, App)
