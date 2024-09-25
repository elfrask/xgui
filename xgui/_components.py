from xgui._class import Vector2
import tkinter
from ._template import (Element)
from ._class import (parse_class_style)

class app(Element):

    tagName = "app"
    lang = "en"
    type = "xgui"

    def __ready(self):

        self.lang = self.params.get("lang", self.lang)
        self.type = self.params.get("type", self.type)

        return 

    pass

class frame(Element):

    tagName = "frame"


    def render(self, _Position: Vector2 = Vector2(), _Size: Vector2 = Vector2(), **_rest):

        tkinter.Frame(self.__MASTER)
        _st = parse_class_style(self.classname,  self.rootDOM.styleSheets)

        for i in self.children:

            child: Element = i
            child.render(_Position + self.style.position, _Size + self.style.size, **_rest)

        return 


    pass


