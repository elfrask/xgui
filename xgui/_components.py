from ._class import Vector2
import tkinter
from ._template import (Element, parse_class_style, get_master)
import debugpy
# from ._class import ()

class app(Element):

    tagName = "app"
    lang = "en"
    type = "xgui"
    isContainable = True

    # def __init__(self, params: dict = ..., parent=None, _MASTER: tkinter.Tk = None, _DOM=None):
    #     super().__init__(params, parent, _MASTER, _DOM)

    def ready(self):

        self.lang = self.params.get("lang", self.lang)
        self.type = self.params.get("type", self.type)

        return 
    def render(self, _Position: Vector2 = ..., _Size: Vector2 = ..., **_rest):
        
        
        _st = self.style


        _APP = tkinter.Frame(self.MASTER,
            bg=_st.backgroundColor.toHex3(),
        )

        self.instance_control = _APP
    
        _APP.pack(fill=tkinter.BOTH, expand=True, side="left")

        self.next(_Position, _Size, _rest)
        


        
    pass

class frame(Element):

    tagName = "frame"
    isContainable = True

    # def __init__(self, params: dict = ..., parent=None, _MASTER: tkinter.Tk = None, _DOM=None):
    #     super().__init__(params, parent, _MASTER, _DOM)

    def render(self, _Position: Vector2 = Vector2(), _Size: Vector2 = Vector2(), **_rest):

        # _st = parse_class_style(self.classname,  self.rootDOM.styleSheets)
        _st = self.style
        _FRAME = tkinter.Frame(get_master(self.parent, self.MASTER, self), 
            bg= _st.backgroundColor.toHex3(),
            width=_st.size.x,
            height=_st.size.y,

            bd=_st.borderWidth,
            highlightcolor=_st.borderColor.toHex3(),
            relief=_st.border,

            # cursor=""
            
        )

        


        

        self.instance_control = _FRAME
        self.display(_FRAME, _st)
    


        self.next(_Position, _Size, _rest)


        pass


    pass

class label(Element):

    tagName= "label"
    text = ""

    # def __init__(self, params: dict = ..., parent=None, _MASTER: tkinter.Tk = None, _DOM=None):
    #     super().__init__(params, parent, _MASTER, _DOM)
    def ready(self):

        # print("_ready")

        self.text = self.innerText


    def render(self, _Position: Vector2 = Vector2(), _Size: Vector2 = Vector2(), **_rest):

        _st = parse_class_style(self.classname,  self.rootDOM.styleSheets)
        _P = get_master(self.parent, self.MASTER, self)
        _LABEL = tkinter.Label(_P, 
            bg=_st.backgroundColor.toHex3(),
            # bg=None,
            # width=_st.size.x,
            # height=_st.size.y,

            bd=_st.borderWidth,
            highlightcolor=_st.borderColor.toHex3(),
            relief=_st.border,

            text=self.text,
            # fg=_st.fontColor.toHex3(),
            fg="red",
            font=(_st.fontFamily, _st.fontSize),

        
            
        )

        # print(_st.getObject())
        # print(self.text)

        
        

        self.instance_control = _LABEL
        self.display(_LABEL, _st)

    


        self.next(_Position, _Size, _rest)

        return 

