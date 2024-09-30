import xml.etree.ElementTree as ET
import tkinter, io
from ._template import (StyleSheets, Style, Element, parse_class_style)
from . import _components as COMPONENTS
from ._class import (Vector2)
# from ._class import (parse_class_style)

# from tkinter import (Label)

DEFAULT_COMPONENTS = {
    "app": COMPONENTS.app,
    "frame": COMPONENTS.frame,
    "label": COMPONENTS.label,
    "button":COMPONENTS.button,
    "prompt": COMPONENTS.prompt,
}

class DOM:

    root = {}
    __list_ids:{Element} = {}
    __data:ET.Element = {}
    __dist:Element
    styleSheets:StyleSheets = StyleSheets({})
    __Components:dict
    __root_engine:tkinter.Tk = None


    def __init__(self, data: str|io.TextIOWrapper, Components:dict = DEFAULT_COMPONENTS, _root = None):
        
        if isinstance(data, io.TextIOWrapper):
            data = data.read()
        
        self.__data = ET.fromstring(data)
        self.__Components = Components
        self.__root_engine = _root
        self.__dist = []
        # self.__list_ids = {}
        # self.update()

        pass

    def setRoot(self, Root):

        self.root = Root
    
    def __compile(self, _DATA:ET.Element, _PARENT: Element = None):

        NodeComponent = self.__Components.get(_DATA.tag, None)

        if NodeComponent == None:

            raise NameError(f"'{_DATA.tag}' is not a component register")
        
        if _DATA.text == None:
            _DATA.text = ""
        
        NE: Element = NodeComponent(_DATA.attrib, _DATA.text.strip(), _PARENT, self.__root_engine, self)
        
        # NE.tagName = _DATA.tag
        
        # NE.style = parse_class_style(NE.classname,  self.styleSheets)

        if "id" in _DATA.attrib.keys():
            self.__list_ids[_DATA.attrib["id"]] = NE
            
        _list =  list(_DATA)
        for child in _list:
            
            NE_child = self.__compile(child, NE)
            NE.addChild(NE_child)

            pass

        return NE

    def build(self):

        self.__list_ids = {}
        
        self.__dist = self.__compile(self.__data)

        pass

    def update(self):

        self.__dist.clean()
        self.__dist.render(Vector2(0, 0), Vector2(0, 0))

        pass
    
    def getById(self, id:str):

        return self.__list_ids.get(id, None)

    def getTreeBuild(self):

        return self.__dist
    
    def render(self, _MASTER:tkinter.Tk = None):

        if _MASTER != None:
            self.__root_engine = _MASTER
        
        self.__dist.clean()
        self.__dist.render(Vector2(0, 0), Vector2(0, 0))
        

        pass
    
    
    pass

class App:

    __MASTER: tkinter.Tk
    doc:DOM
    __styleSheets: StyleSheets
    __x = 0
    __y = 0

    __width = 100
    __height = 100

    __data = []
    __title = "untitled"
    

    __components = {}
    # __root_app: tkinter.Tk



    def __init__(self, COMPONENTS=DEFAULT_COMPONENTS):

        self.__components = COMPONENTS
        self.__MASTER = tkinter.Tk()
        
        pass

    def size(self, width = 100, height = 100):

        self.__width = width
        self.__height = height
    def position(self, x = 0, y = 0):

        self.__x = x
        self.__y = y
    def build(self, data, styleSheets:StyleSheets=StyleSheets({}), x=0, y=0, width=100, height=100):

        self.__y = y
        self.__x = x
        self.__width = width
        self.__height = height

        
        self.doc = DOM(data, self.__components, self.__MASTER)
        self.doc.styleSheets = styleSheets
        self.__styleSheets = styleSheets

        self.doc.build()

        return self.doc
    
    def title(self, title:str):

        self.__title = title
    
    def load(pathXml: io.TextIOWrapper, pathStyle: io.TextIOWrapper, COMPONENTS=DEFAULT_COMPONENTS):
        _xml = pathXml.read()
        _style = pathStyle.read()
        
        _style_dist = StyleSheets(_style)
        _app = App(COMPONENTS)
        _app.build(_xml, _style_dist)

        return _app
    def run(self):

        def run_app(): 
            self.__MASTER.mainloop()

        self.__MASTER.title(self.__title)
        self.__MASTER.geometry(f"{self.__width}x{self.__height}")
        
        self.doc.render()

        run_app()

        pass

    pass