from xgui._class import Vector2
import tkinter
from ._template import (Element, parse_class_style, get_master)
# from ._class import ()

class app(Element):

    tagName = "app"
    lang = "en"
    type = "xgui"
    isContainable = True

    def __init__(self, params: dict = ..., parent=None, _MASTER: tkinter.Tk = None, _DOM=None):
        super().__init__(params, parent, _MASTER, _DOM)

    def __ready(self):

        self.lang = self.params.get("lang", self.lang)
        self.type = self.params.get("type", self.type)

        return 
    def render(self, _Position: Vector2 = ..., _Size: Vector2 = ..., **_rest):
        
        _st = parse_class_style(self.classname,  self.rootDOM.styleSheets)

        print(self.MASTER)

        _APP = tkinter.Frame(self.MASTER,
            bg=_st.backgroundColor.toHex3()
        )

        self.instance_control = _APP
    
        _APP.pack(fill=tkinter.BOTH, expand=True)

        for i in self.children:

            child: Element = i
            child.render(_Position + self.style.position, _Size + self.style.size, **_rest)


        
    pass

class frame(Element):

    tagName = "frame"
    isContainable = True

    def __init__(self, params: dict = ..., parent=None, _MASTER: tkinter.Tk = None, _DOM=None):
        super().__init__(params, parent, _MASTER, _DOM)

    def render(self, _Position: Vector2 = Vector2(), _Size: Vector2 = Vector2(), **_rest):

        # _st = parse_class_style(self.classname,  self.rootDOM.styleSheets)
        _st = self.style
        _FRAME = tkinter.Frame(get_master(self.parent, self.MASTER), 
            bg=_st.backgroundColor.toHex3(),
            width=_st.size.x,
            height=_st.size.y
            
        )

        

        self.instance_control = _FRAME
        self.display(_FRAME, _st)
    


        for i in self.children:

            child: Element = i
            child.render(_Position + self.style.position, _Size + self.style.size, **_rest)

        return 


    pass

class label(Element):

    tagName= "label"

    def __init__(self, params: dict = ..., parent=None, _MASTER: tkinter.Tk = None, _DOM=None):
        super().__init__(params, parent, _MASTER, _DOM)

    def render(self, _Position: Vector2 = Vector2(), _Size: Vector2 = Vector2(), **_rest):

        _st = parse_class_style(self.classname,  self.rootDOM.styleSheets)

        _FRAME = tkinter.Frame(get_master(self.parent, self.MASTER), 
            bg=_st.backgroundColor.toHex3(),
            width=_st.size.x,
            height=_st.size.y
            
        )

        

        self.instance_control = _FRAME
    


        for i in self.children:

            child: Element = i
            child.render(_Position + self.style.position, _Size + self.style.size, **_rest)

        return 

