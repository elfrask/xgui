from xgui._class import Vector2
import tkinter
from ._template import (Element, parse_class_style)
# from ._class import ()

class app(Element):

    tagName = "app"
    lang = "en"
    type = "xgui"

    def __ready(self):

        self.lang = self.params.get("lang", self.lang)
        self.type = self.params.get("type", self.type)

        return 
    def render(self, _Position: Vector2 = ..., _Size: Vector2 = ..., **_rest):
        
        _st = parse_class_style(self.classname,  self.rootDOM.styleSheets)

        _APP = tkinter.Frame(self.__MASTER)

        self.__instance_control = _APP
    
        _APP.pack(fill=tkinter.BOTH, expand=True)

        for i in self.children:

            child: Element = i
            child.render(_Position + self.style.position, _Size + self.style.size, **_rest)


        
    pass

class frame(Element):

    tagName = "frame"


    def render(self, _Position: Vector2 = Vector2(), _Size: Vector2 = Vector2(), **_rest):

        _st = parse_class_style(self.classname,  self.rootDOM.styleSheets)

        _FRAME = tkinter.Frame(self.__MASTER, 
            bg=_st.backgroundColor,
            width=_st.size.x,
            height=_st.size.y
            
        )

        

        self.__instance_control = _FRAME
    


        for i in self.children:

            child: Element = i
            child.render(_Position + self.style.position, _Size + self.style.size, **_rest)

        return 


    pass

class label(Element):

    tagName= "label"

    def render(self, _Position: Vector2 = Vector2(), _Size: Vector2 = Vector2(), **_rest):

        _st = parse_class_style(self.classname,  self.rootDOM.styleSheets)

        _FRAME = tkinter.Frame(self.__MASTER, 
            bg=_st.backgroundColor,
            width=_st.size.x,
            height=_st.size.y
            
        )

        

        self.__instance_control = _FRAME
    


        for i in self.children:

            child: Element = i
            child.render(_Position + self.style.position, _Size + self.style.size, **_rest)

        return 

