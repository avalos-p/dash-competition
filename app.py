import dash
from dash import Dash, html, dcc
from dash_bootstrap_components.themes import BOOTSTRAP


def main()-> None:
    app = Dash(__name__, use_pages=True, external_stylesheets=[BOOTSTRAP])
    app.config.suppress_callback_exceptions = True
    app.layout = html.Div([
        html.H1('Dash Competition: Credit Card transactions fraud detection with Machine Learning'),
        html.H2('April - 2024', className='date-project'),  
        html.Div([
            dcc.Link(
                html.Button(f"{page['name']}", className='button-links'), 
                href=page["relative_path"]
            )
            for page in dash.page_registry.values()
        ],className='buttons-div'),

        dash.page_container])
    return app


if __name__ == '__main__':
    app = main()
    server = app.server
    app.run_server(debug=True)
