import xml.etree.ElementTree as ET
import tkinter, io
from ._template import (StyleSheets, Style, Element)

# from tkinter import (Label)

DEFAULT_COMPONENTS = {
    **{}
}

class DOM:

    root = {}
    __list_ids:{Element} = {}
    __data:ET.Element = {}
    __dist = []
    styleSheets:StyleSheets
    __Components = {}


    def __init__(self, data: str|io.TextIOWrapper, Components:dict = DEFAULT_COMPONENTS):
        
        if isinstance(data, io.TextIOWrapper):
            data = data.read()
        
        self.__data = ET.fromstring(data)
        self.__Components = Components
        self.update()

        pass

    def setRoot(self, Root):

        self.root = Root
    
    def __compile(self, _DATA:ET.Element, _PARENT: Element = None):

        NodeComponent = self.__Components.get(_DATA.tag, None)

        if NodeComponent == None:

            raise NameError(f"'{_DATA.tag}' is not a component register")
        
        NE: Element = NodeComponent(_DATA.attrib, _PARENT)
        NE.tagName = _DATA.tag
        NE.innerText = _DATA.text

        if "id" in _DATA.attrib.keys():
            self.__list_ids[child.attrib["id"]] = NE
            

        for child in _DATA:
            
            NE_child = self.__compile(child)
            NE.addChild(NE_child)

            pass

        return NE

    def update(self):

        self.__list_ids = {}
        
        self.__dist = self.__compile(self.__data)

        pass
    
    def getById(self, id:str):

        return self.__list_ids.get(id, None)

    def getTreeBuild(self):

        return self.__dist
    pass

class App:

    MASTER: tkinter.Tk
    doc:DOM
    __styleSheets: StyleSheets
    __x = 0
    __y = 0

    __width = 100
    __height = 100

    __data = []
    __components:{} = {}



    def __init__(self, COMPONENTS=DEFAULT_COMPONENTS):

        self.__components = COMPONENTS
        
        pass
    
    def build(self, data, styleSheets:StyleSheets=StyleSheets({}), x=0, y=0, width=100, height=100):

        self.__y = y
        self.__x = x
        self.__width = width
        self.__height = height

        
        self.doc = DOM(data, self.__components)
        self.__styleSheets = styleSheets
        self.doc.styleSheets = styleSheets

        return self.doc

    pass