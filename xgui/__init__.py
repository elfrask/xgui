# XGUI is a graphic library that use xml for design graphics interface



from . import (version as VERSiON)
from ._class import (COLORS, rgba, Vector2)
from ._template import (Style, StyleSheets, Element)
from . import _components as Components 
from ._window import (App, DEFAULT_COMPONENTS)
from ._components import (button, label, frame, app as app_element, prompt)

