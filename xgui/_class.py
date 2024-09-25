from ._template import (Element, Style, StyleSheets)

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

class rgba:
    RED = 0
    GREEN = 0
    BLUE = 0
    ALPHA = 0

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

    def totuple(self):

        return (self.RED, self.GREEN, self.BLUE, self.ALPHA)
    
    def parse(value):

        if isinstance(value, str):

            return getattr(COLORS, value.upper())

        return

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


    pass

def parse_class_style(class_style: str, _SS: StyleSheets) -> Style:

    _class = class_style.split(" ")
    _out = Style()
    for i in _class:
        if not i in ["", "\t", "\n", "\r"]:
            _out.set(_SS.getClass(i))

    return _out