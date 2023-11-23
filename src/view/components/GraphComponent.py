from dash import dcc

from .IComponent import IComponent


class GraphComponent(IComponent):

    def __init__(self, id: str):
        super().__init__(id)
        self.graph = dcc.Graph(id=self.id, figure={})

    def update_graph(self, figure):
        self.graph = dcc.Graph(id=self.id, figure=figure)

    def render(self):
        return self.graph