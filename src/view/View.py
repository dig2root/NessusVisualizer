import dash
import dash_bootstrap_components as dbc
from dash import html

from src.view.components.NavbarComponent import NavbarComponent
from src.view.components.DropdownComponent import DropdownComponent
from src.view.components.GraphComponent import GraphComponent
from src.view.components.UploadComponent import UploadComponent


class View(dash.Dash):

    NESSUS_UPLOAD_FOLDER_ROOT = "./data/uploads"
    INSTANCE = None

    def __init__(self, title: str = None):
        super().__init__(external_stylesheets=[dbc.themes.FLATLY])
        self.title = "NessusVisualizer v0.1.0"
        self.layout = self.define_layout()

    @staticmethod
    def get_instance():
        if View.INSTANCE is None:
            View.INSTANCE = View()
        return View.INSTANCE

    def initialize(self):
        self.initialize_components()

    def initialize_components(self):
        self.navbar = NavbarComponent("navbar")
        self.upload = UploadComponent("nessus-uploader", self, self.NESSUS_UPLOAD_FOLDER_ROOT)
        self.dropdown = DropdownComponent("nessus-dropdown")
        self.graph = GraphComponent("graph")

    def define_layout(self):
        self.initialize()
        return html.Div([
            self.navbar.render(),   
            self.upload.render(),
            self.dropdown.render(),
            self.graph.render()
            ],
            style={
                'width': '100%',
                'display': 'inline-block'
            }
        )