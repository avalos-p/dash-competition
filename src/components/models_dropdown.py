from dash import Dash, dcc, html
from dash.dependencies import Input, Output

from . import ids
import json

'''
Importing data
'''
with open('data/modelos_dic.json', 'r') as json_file:
    models_dict = json.load(json_file)

# Ordering by accuracy
models_order = sorted(models_dict.items(), key=lambda x: x[1]['accuracy'], reverse=True)
models_order = [(nombre, datos['accuracy']) for nombre, datos in models_order]
models_names = [(nombre) for nombre,datos in models_order]

models_names_original = models_names


def render(app: Dash) -> html.Div:

    @app.callback(
        Output(ids.MODELS_DROPDOWN, "value"),
        Input(ids.SELECT_ALL_MODELS_BUTTON, "n_clicks"),
    )
    def select_all_modelss(_: int) -> list[str]:
        return models_names_original

    return html.Div(
        children=[
            html.H6("Model"),
            dcc.Dropdown(
                id=ids.MODELS_DROPDOWN,
                options=[{"label": name, "value": name} for name in models_names],
                value=models_names_original,
                multi=True,
            ),
            html.Button(
                className="dropdown-button",
                children=["Select All"],
                id=ids.SELECT_ALL_MODELS_BUTTON,
                n_clicks=0,
            ),
        ]
    )
