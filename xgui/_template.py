from ._class import (COLORS, rgba, Vector2, clamp, DICT_COLORS, attrib2dict, Cross)
import importlib
from termcolor import (colored as col)
import tkinter
import os
import xml.etree.ElementTree as ET

os.system("color")


__list_properties = {
    "size":"size",
    "position":"position",
    "margin":"margin",
    "padding":"padding",

    "display":"display",

    # Pack Display Options
    "align":"align",
    "expand":"expand",
    "fill":"fill",



    "backgroundColor": "background-color",

    "fontFamily": "font-family",
    "fontSize": "font-size",
    "fontColor": "font-color",
    
    "borderColor":"border-color",
    "borderWidth":"border-width",
    
    # "hAlign":"h-align",
    
}

class DISPLAYS:

    PACK = "pack"
    PLACE = "place"
    GRID = "grid"
    NONE = "none"

class Style:

    CLASSNAME = ""
    __dict_style = {}
    

    size: Vector2 = Vector2()
    position: Vector2 = Vector2()
    margin: Vector2 = Vector2()
    padding: Vector2 = Vector2()
    # padding: Cross = Cross()
    
    display: str = "pack"

    align:str = tkinter.LEFT
    expand:bool = False
    fill:str = tkinter.NONE
    # vAlign = "start"

    backgroundColor: rgba = COLORS.WHITE

    fontFamily: str = "Arial"
    fontSize: int = 12
    fontColor: rgba = COLORS.BLACK

    borderColor: rgba = COLORS.BLACK
    borderWidth: int = 0


    def __init__(self, data={}, classname=""):

        self.CLASSNAME = classname
        self.__dict_style = {}
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
                            print(col(f"WARNING: the value of attribute '{i}' of the class '{self.CLASSNAME}' it is not valid", "yellow"))
                        pass

                    pass
                else:
                    if show_logs:
                        print(col(f"WARNING: the value of attribute '{i}' of class '{self.CLASSNAME}' it is not valid", "yellow"))

                    pass

                pass
            else:
                if show_logs:
                    print(col(f"WARNING: the attribute '{i}' of the class '{self.CLASSNAME}' is not a style attribute", "yellow"))
                pass


        pass
    def __repr__(self) -> str:


        return f"{col('Style', 'light_blue')}: ({col('name', 'light_green')}: {col(self.CLASSNAME, 'yellow')})"

    def getObject(self):

        return self.__dict_style

    def getObjectFromStyle(self):

        _out = {}

        for i in __list_properties:

            _out[__list_properties[i]] = getattr(self, i)
            pass

        return _out

    pass    

class StyleSheets:

    classTags = {}

    def __init__(self, data={}) -> None:

        self.classTags = {}

        if isinstance(data, str):
            data = eval(data, {
                # class and functions
                "rgba": rgba,
                "Vector2": Vector2,
                "Cross": Cross,
                
                # constants
                **DICT_COLORS,

                "left": tkinter.LEFT,
                "right": tkinter.RIGHT,
                "top": tkinter.TOP,
                "bottom": tkinter.BOTTOM,
                
                "both": tkinter.BOTH,
                "none": tkinter.NONE,
                "x": tkinter.X,
                "y": tkinter.Y,

                "pack": DISPLAYS.PACK,
                "place": DISPLAYS.PLACE,
                "grid": DISPLAYS.GRID,


            })
            pass
            
        for i in data:

            self.classTags[i] = Style(data[i], i)

            pass

        pass

    def getClass(self, classname:str) -> Style:

        return self.classTags.get(classname, {})

    def __repr__(self) -> str:

        _li = []

        for i in self.classTags:

            _li.append(col(i, "yellow"))

        return f"StyleSheets: ({ ', '.join(list(_li)) })"

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
        self.__EVENTS = {}
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
    children:dict = []
    id: str|None = None
    style: Style 
    innerText:str = ""
    events:Event
    # rootDOM: DOM
    rootDOM:object = None
    classname = ""
    isContainable:bool = False
    instance_control: tkinter.Widget = None
    MASTER: tkinter.Tk = None



    def __init__(self, params:dict={}, parent=None, _MASTER:tkinter.Tk = None, _DOM = None):
        
        self.params = params
        self.id = params.get("id", None)
        self.classname = params.get("class", "")
        self.events = Event(self)
        self.MASTER = _MASTER
        self.rootDOM = _DOM
        self.children = []

        if isinstance(_DOM, DOM):
            self.style = parse_class_style(self.classname, self.rootDOM.styleSheets)

        # self.children = children
        self.__ready()

        pass
    def __ready(self):

        pass
    def display(self, _Widget: tkinter.Widget, _Style: Style):

        _display = _Style.display

        if _display == DISPLAYS.PACK:

            _Widget.pack(
                side=_Style.align,
                expand=_Style.expand,
                fill=_Style.fill,

                padx=_Style.margin.x,
                pady=_Style.margin.y,

                ipadx=_Style.padding.x,
                ipady=_Style.padding.y,

                # ipadx=(_Style.padding.right, _Style.padding.left),
                # ipady=(_Style.padding.top, _Style.padding.bottom)

            )

            pass
        elif _display == DISPLAYS.NONE:

            pass


        pass
    def setParent(self, parent):

        self.parent = parent    
    def addChild(self, child):

        self.children.append(child)
    def render(self, _Position: Vector2 = Vector2(), _Size: Vector2 = Vector2(), **_rest):

        for i in self.children:

            child: Element = i
            child.render(_Position + self.style.position, _Size + self.style.size, **_rest)
            

        pass
    def __repr__(self) -> str:

        _params = ""

        _c_params = list(self.params)

        

        for i in _c_params:
            _t = '"'
            _params += f" {col(i, 'light_green')}={ col( _t + self.params[i] + _t, 'yellow') }"
            pass
        
        # print(_c_params)

        _color_tagname = col(self.tagName, "light_red")

        return f"<{_color_tagname}{_params}> {col('...', 'blue')} </{_color_tagname}>"
    
    
    pass



def parse_class_style(class_style: str, _SS:StyleSheets) -> Style:
    # _SS: StyleSheets = _SS

    _class = class_style.split(" ")
    _out = Style()
    for i in _class:
        if not i in ["", "\t", "\n", "\r"]:
            _out.set(_SS.getClass(i).getObject())

    return _out

def get_master(_Element: Element, _Master: tkinter.Tk):

    _out: Element = _Element

    while True:
        if _out == None:
            return _Master

        if _out.isContainable:
            return _out
        elif not _out.isContainable:
            _out = _out.parent
            continue


from ._window import (DOM, App)
