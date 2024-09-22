from ._class import (COLORS, rgba, Vector2)
import termcolor
import os

os.system("color")

class Style:

    CLASSNAME = ""

    size: Vector2 = Vector2()
    position: Vector2 = Vector2()
    
    positionMode: str = "relative"
    backgroundColor: rgba = COLORS.WHITE

    fontFamily: str = "Arial"
    fontSize: int = 12
    fontColor: rgba = COLORS.BLACK

    hAlign = "start"
    vAlign = "start"

    def __init__(self, data={}, classname=""):

        self.CLASSNAME = classname
        self.set(data)

        pass

    def set(self, data={}):

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
                    except Exception as err:
                        print(termcolor.colored(f"WARNING: the value of attribute '{i}' of the class '{self.CLASSNAME}' it is not valid", "yellow"))


                        pass

                    

                    pass
                else:
                    print(termcolor.colored(f"WARNING: the value of attribute '{i}' of class '{self.CLASSNAME}' it is not valid", "yellow"))

                    pass

                pass
            else:
                print(termcolor.colored(f"WARNING: the attribute '{i}' of the class '{self.CLASSNAME}' is not a style attribute", "yellow"))
                pass


        pass
    def __repr__(self) -> str:
        return f"Style: (name: {self.CLASSNAME})"

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

    def __repr__(self) -> str:

        return f"StyleSheets: ({ ', '.join(list(self.classTags)) })"

    pass



class Element:

    TagName = "frame"
    params = {}


    def __init__(self, params={}):
        


        pass

    pass