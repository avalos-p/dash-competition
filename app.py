import dash
from dash import Dash, html, dcc
from dash_bootstrap_components.themes import BOOTSTRAP


def main()-> None:
    app = Dash(__name__, use_pages=True, external_stylesheets=[BOOTSTRAP])
    app.config.suppress_callback_exceptions = True
    app.layout = html.Div([
        html.H1('Credit Card transactions fraud detection using Machine Learning'),
        html.Hr(),
        html.Div([
            dcc.Link(
                html.Button(f"{page['name']}", className='button-links'), 
                href=page["relative_path"]
            )
            for page in dash.page_registry.values()
        ]),

        dash.page_container])
    return app


if __name__ == '__main__':
    app = main()
    app.run_server(debug=True)
