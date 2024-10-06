# from ._template import (Element, Style, StyleSheets)
import tkinter

def clamp(value, min, max):

    out = value

    if min > value: value = min
    if max < value: value = max

    return value

class Vector2:

    x:float = 0
    y:float = 0

    def __init__(self, x:float = 0, y:float = 0) -> None:
        
        self.x = x
        self.y = y

        pass
    def parse(value: float):

        return Vector2(value, value)
    def __add__(self, value):

        return Vector2(
            self.x + value.x,
            self.y + value.y
        )
    def __sub__(self, value):

        return Vector2(
            self.x - value.x,
            self.y - value.y
        )
    def __mul__(self, value):

        return Vector2(
            self.x * value.x,
            self.y * value.y
        )
    def __truediv__(self, value):

        return Vector2(
            self.x / value.x,
            self.y / value.y
        )
    def __pow__(self, value):

        return Vector2(
            self.x ** value.x,
            self.y ** value.y
        )
    def __mod__(self, value):

        return Vector2(
            self.x % value.x,
            self.y % value.y
        )
    def __repr__(self) -> str:
        return f"Vector2({self.x}, {self.y})"
    
    pass

class Cross:

    top:float = 0
    bottom:float = 0
    right:float = 0
    left:float = 0


    def __init__(self, top:float = 0, bottom:float = 0, right:float = 0, left:float = 0,) -> None:
        
        self.top = top
        self.bottom = bottom
        self.right = right
        self.left = left

        pass
    def parse(value: float):

        return Cross(value, value, value, value)
    def __add__(self, value):

        return Cross(
            self.top + value.top,
            self.bottom + value.bottom,
            self.right + value.right,
            self.left + value.left
        )
    def __sub__(self, value):

        return Cross(
            self.top - value.top,
            self.bottom - value.bottom,
            self.right - value.right,
            self.left - value.left
        )
    def __mul__(self, value):

        return Cross(
            self.top * value.top,
            self.bottom * value.bottom,
            self.right * value.right,
            self.left * value.left
        )
    def __truediv__(self, value):

        return Cross(
            self.top / value.top,
            self.bottom / value.bottom,
            self.right / value.right,
            self.left / value.left
        )
    def __pow__(self, value):

        return Cross(
            self.top ** value.top,
            self.bottom ** value.bottom,
            self.right ** value.right,
            self.left ** value.left
        )
    def __mod__(self, value):

        return Cross(
            self.top % value.top,
            self.bottom % value.bottom,
            self.right % value.right,
            self.left % value.left
        )
    def __repr__(self) -> str:
        return f"Cross({self.top}, {self.bottom}, {self.right}, {self.left})"
    
    pass



class rgba:
    RED: int = 0
    GREEN: int = 0
    BLUE: int = 0
    ALPHA: float = 0

    def __init__(self, red: float, green: float, blue: float, alpha:float = 0.0) -> None:
        
        self.RED = clamp(red, 0, 255)
        self.GREEN = clamp(green, 0, 255)
        self.BLUE = clamp(blue, 0, 255)
        self.ALPHA = clamp(alpha, 0, 1)

        

        
        pass

    def __repr__(self) -> str:

        return f"rgba({self.RED}, {self.GREEN}, {self.BLUE}, {self.ALPHA})"
    
    def tohex(self) -> str:

        def ti(value):

            if len(value) < 2:
                return "0" + value

            return value

        return "#" + ti(hex(self.RED)[2:]) + ti(hex(self.GREEN)[2:]) + ti(hex(self.BLUE)[2:]) + ti(hex(int(self.ALPHA * 255))[2:]) 

    def toHex3(self):

        return f'#{self.RED:02x}{self.GREEN:02x}{self.BLUE:02x}'

    def totuple(self):

        return (self.RED, self.GREEN, self.BLUE, self.ALPHA)
    
    def square(value):

        return Vector2(value, value)

    def parse(value):

        if isinstance(value, str):

            return getattr(COLORS, value.upper())
        elif isinstance(value, Vector2):
            
            return value
        elif value.__class__ in [int, float]:
            
            return Vector2(value, value)
        

        raise Exception(f"the value '{value.__class__.__name__}' it's not parsable for Vector2")

class COLORS:

    RED = rgba(255, 0, 0, 1)
    GREEN = rgba(0, 255, 0, 1)
    BLUE = rgba(0, 0, 255, 1)

    YELLOW = rgba(255, 255, 0, 1)
    MAGENTA = rgba(255, 0, 255, 1)
    CYAN = rgba(0, 255, 255, 1)

    PURPLE = rgba(40, 0, 124, 1)
    ORANGE = rgba(255, 135, 0, 1)
    LIME = rgba(157, 255, 0, 1)
    TURQUOISE = rgba(0, 255, 114, 1)

    TRANSPARENT = rgba(0, 0, 0, 0)

    BLACK = rgba(0, 0, 0, 1)
    WHITE = rgba(255, 255, 255, 1)
    GRAY = rgba(130, 130, 130, 1)
    GRAY0 = rgba(240, 240, 240, 1)
    GRAY1 = rgba(222, 222, 222, 1)
    GRAY2 = rgba(199, 199, 199, 1)
    GRAY3 = rgba(181, 181, 181, 1)
    GRAY4 = rgba(163, 163, 163, 1)
    GRAY5 = rgba(140, 140, 140, 1)
    GRAY6 = rgba(120, 120, 120, 1)
    GRAY7 = rgba(101, 101, 101, 1)

    GRAY8 = rgba(86, 86, 86, 1)
    GRAY9 = rgba(68, 68, 68, 1)
    GRAY10 = rgba(57, 57, 57, 1)
    GRAY11 = rgba(40, 40, 40, 1)
    GRAY12 = rgba(25, 25, 25, 1)
    GRAY13 = rgba(17, 17, 17, 1)


    pass

def attrib2dict(obj) -> dict:
    _out = {}
    
    for i in dir(obj):

        if not i[:2] == "__":

            _out[i.lower()] = getattr(obj, i)
            pass

        pass
    return _out

DICT_COLORS = attrib2dict(COLORS)







# from ._template import (StyleSheets, Style, Element)


# def render(_Obj: tkinter.Widget, _Style: Style, _Element: Element):

#     pass