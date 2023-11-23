import dash
import os

from src.view.View import View
from src.controller.Controller import Controller

# Initialize the app
view = View.get_instance()
controller = Controller.get_instance()

# Callback for uploading files
@view.callback(
    dash.dependencies.Output("nessus-dropdown", "options"),
    dash.dependencies.Input('nessus-uploader', 'isCompleted'))
def update_dropdown(isCompleted):
    subfolders = os.listdir(view.upload.get_upload_folder())
    file_names = []
    for subfolder in subfolders:
        file_names.extend(os.listdir(os.path.join(view.upload.get_upload_folder(), subfolder)))
    return file_names

# Callback for dropdown value
@view.callback(
    dash.dependencies.Output("nessus-dropdown", "value"),
    dash.dependencies.Input('nessus-dropdown', 'value'))
def display_graph(value):
    controller.get_vulnerabilities_from_xml()
    return None

if __name__ == '__main__':
    view.run_server(debug=True)