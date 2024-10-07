from ._class import Vector2, COLORS, rgba
import tkinter
from ._template import (Element, parse_class_style, get_master, Style)
import debugpy
# from ._class import ()

def _exclude(_dic = {}, _excl = []):

    _out = {}

    for i in _dic:
        if not i in _excl:
            _out[i] = _dic[i]
    
    return _out

def default_params_for_box(_st: Style, _excludes:list[str] = []):

    return _exclude({

        "bg":_st.backgroundColor.toHex3(),

        "width": _st.size.x,
        "height": _st.size.y,

        "bd":_st.borderWidth,
        "highlightcolor":_st.borderColor.toHex3(),
        "relief":_st.border,

    }, _excludes)
def default_params_for_text(_st: Style, _excludes:list[str] = []):

    return _exclude({

        "fg":_st.fontColor.toHex3(),
        "font": (_st.fontFamily, _st.fontSize),

        "justify":_st.justify
    }, _excludes)

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
            **default_params_for_box(_st)
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

        
        _st = self.style

        _P = get_master(self.parent, self.MASTER, self)

        # print()
        # print(_st.getObject())
        # print(self.text)

        _LABEL = tkinter.Label(_P,
            
            **default_params_for_box(_st),
            **default_params_for_text(_st),

            text=self.text,
            
            
        
            
        )
        

        
        

        self.instance_control = _LABEL
        self.display(_LABEL, _st)

    


        self.next(_Position, _Size, _rest)

        return 

class button(Element):

    tagName= "button"
    text = ""
    defaultElementStyle = {
        "border":"raised",
        "border-width": 3,
        "background-color": COLORS.GRAY1
    }

    # def __init__(self, params: dict = ..., parent=None, _MASTER: tkinter.Tk = None, _DOM=None):
    #     super().__init__(params, parent, _MASTER, _DOM)
    def ready(self):

        # print("_ready")

        self.text = self.innerText


    def render(self, _Position: Vector2 = Vector2(), _Size: Vector2 = Vector2(), **_rest):

        _st = self.style
        _P = get_master(self.parent, self.MASTER, self)
        _BUTTON = tkinter.Button(_P, 
            
            **default_params_for_box(_st),
            **default_params_for_text(_st),
            
            text=self.text,
            command=self.events.callClick, 
            
            
            
        )
        
        # print(_st.getObject())
        # print(self.text)

        
        

        self.instance_control = _BUTTON
        self.display(_BUTTON, _st)

    


        self.next(_Position, _Size, _rest)

        return
    
class prompt(Element):

    tagName= "prompt"
    value = ""
    defaultElementStyle = {
        "border":"sunken",
        "border-width": 3,
        "size": Vector2(10, 0)
    }

    # def __init__(self, params: dict = ..., parent=None, _MASTER: tkinter.Tk = None, _DOM=None):
    #     super().__init__(params, parent, _MASTER, _DOM)
    def ready(self):

        # print("prompt:", self.style.border)
        
        self.value = self.params.get("value", "")


    def render(self, _Position: Vector2 = Vector2(), _Size: Vector2 = Vector2(), **_rest):

        # _st = self.StyleFromParams()
        _st = self.style
        _P = get_master(self.parent, self.MASTER, self)

        # print(_st.getObject())

        _ENTRY = tkinter.Entry(_P, 
            
            **default_params_for_box(_st, ["height"]),
            **default_params_for_text(_st),
            
            # text=self.text,
            # command=self.events.callClick, 
            # invcmd=
            
            
            
        )

        # _ENTRY.bind("<Key>", self.events.callChange)
        _ENTRY.bind("<KeyRelease>", lambda x: setattr(self, "value", _ENTRY.get()))
        _ENTRY.insert(0, self.value)
        
        # print(self.text)

        
        

        self.instance_control = _ENTRY
        self.display(_ENTRY, _st)

    


        self.next(_Position, _Size, _rest)

        return
    

