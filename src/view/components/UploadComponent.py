import dash_uploader as du
from dash import html

from .IComponent import IComponent


class UploadComponent(IComponent):

    def __init__(self, id: str, app, upload_folder):
        super().__init__(id)
        self.upload_folder = upload_folder
        du.configure_upload(app, self.upload_folder)

    def render(self):
        return html.Div(
            [du.Upload(
                id=self.id,
                filetypes=['nessus'],
                max_file_size=1000,
                max_files=2,
            )],
            style={
                'textAlign': 'center',
                'width': '30%',
                'padding': '25px',
                'display': 'inline-block'
            }
        )

    def get_upload_folder(self):
        return self.upload_folder