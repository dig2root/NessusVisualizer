from dash import dcc
from .IComponent import IComponent


class GraphComponent(IComponent):

    def __init__(self, id: str):
        super().__init__(id)

    def render(self):
        return dcc.Graph(
            id=self.id,
            figure={
                'data': [
                    {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'Vulnerabilities'},
                    {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': 'Hosts'},
                ],
                'layout': {
                    'title': 'Nessus Visualizer'
                }
            }
        )