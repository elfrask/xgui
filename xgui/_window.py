import xml.etree.ElementTree as ET
import tkinter, io
from ._template import (StyleSheets, Style, Element)

# from tkinter import (Label)

DEFAULT_COMPONENTS = {
    **{}
}

class DOM:

    root = {}
    __list_ids = {}
    __data:ET.Element = {}
    __dist = []
    styleSheets:StyleSheets
    __Components = {}


    def __init__(self, data, Components:dict = DEFAULT_COMPONENTS):

        if isinstance(data, io.TextIOWrapper):
            data = data.read()

        self.__data = ET.fromstring(data)

        pass

    def setRoot(self, Root):

        self.root = Root
    
    def update(self):

        def _compile(_DATA:ET.Element):

            Node = self.__Components.get(_DATA.tag, None)

            if Node == None:

                raise NameError(f"'{_DATA.tag}' is not a component register")
            

            for child in _DATA:

                pass

            return
        
        self.__dist = _compile(self.__data)

        pass
    
    def getById(self, id:str):

        return self.__list_ids.get(id, None)

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
        self.doc = styleSheets


        pass

    pass