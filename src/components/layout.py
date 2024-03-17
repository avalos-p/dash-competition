from dash import Dash, html

from . import models_dropdown, percentage_chart


def create_layout(app: Dash) -> html.Div:
    return html.Div(
        className="app-div",
        children=[
            html.H1(app.title),
            html.Hr(),
            html.Div(
                className="dropdown-container",
                children=[
                    models_dropdown.render(app),
                ],
            ),
            percentage_chart.render(app),
        ]
    )
