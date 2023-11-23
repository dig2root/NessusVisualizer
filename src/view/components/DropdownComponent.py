from dash import dcc
from dash import html

from .IComponent import IComponent


class DropdownComponent(IComponent):

    def __init__(self, id: str):
        super().__init__(id)

    def render(self):
        return html.Div(
            [dcc.Dropdown(
            id=self.id,
            options=[],
            value=None,
            )],
            style={
                'textAlign': 'center',
                'width': '30%',
                'padding': '25px',
            }
        )