import dash
import os
import plotly.graph_objs as go
import numpy as np

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
    dash.dependencies.Output("graph", "figure"),
    dash.dependencies.Input('nessus-dropdown', 'value'))
def display_graph(value):
    nodes = controller.get_nodes_from_xml()
    # Create a go.Figure object to display the network graph to display every node in nodes list as a point
    fig = go.Figure(
        data=[],
        layout=go.Layout(
            title="Nessus report nodes",
            titlefont_size=16,
            showlegend=False,
            hovermode='closest',
            margin=dict(b=20,l=5,r=5,t=40),
            xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
            yaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
            width=600,
            height=600
        ))
    # Add nodes
    step = np.pi * 2 / len(nodes)
    current = 0
    for node in nodes:
        x = np.cos(current)
        y = np.sin(current)
        fig.add_trace(go.Scatter(x=[x], y=[y], mode='markers', marker=dict(size=10, color='LightSkyBlue'), text=node))
        current += step
    return fig

if __name__ == '__main__':
    view.run_server(debug=True)