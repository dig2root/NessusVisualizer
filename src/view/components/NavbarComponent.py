import dash_bootstrap_components as dbc
from .IComponent import IComponent

class NavbarComponent(IComponent):

    def __init__(self, id: str):
        super().__init__(id)

    def render(self):
        return dbc.NavbarSimple(
            children=[
                dbc.NavItem(dbc.NavLink("Home", href="#")),
            ],
            brand="NessusVisualizer v0.1.0",
            brand_href="#",
            color="primary",
            dark=True,
        )