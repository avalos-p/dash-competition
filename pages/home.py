import dash
import dash_bootstrap_components as dbc
from dash import Input, Output, dcc, html, callback
from dash.dependencies import Input, Output

dash.register_page(__name__, path='/',name="Introduction")

sidebar = html.Div(
    [dbc.Nav(
            [   
                dbc.NavLink("Introduction to Dash Challenge", href="#introduction",className="sidebar-link",external_link=True),
                dbc.NavLink("Imbalanced Dataset", href="#imbalanced",className="sidebar-link",external_link=True),
                dbc.NavLink("Understanding the Data", href="#dataset",className="sidebar-link",external_link=True),
                dbc.NavLink("Machine Learning Models", href="#ml-models",className="sidebar-link",external_link=True),
                dbc.NavLink("Hyperparemeters", href="#hyperparemeters",className="sidebar-link",external_link=True),
                dbc.NavLink("Results", href="#results",className="sidebar-link",external_link=True),
            ],
            vertical=True,
            pills=True,
        ),
    ],
    className="sidebar-style"
)


content = html.Div([
            html.Div([
                html.H4('Introduction',id='introduction'),
                html.H5('''challenge is all about fraud detection. The challenge is to build a Dash app 
                        that offers data visualization around credit card usage and a prediction element 
                        for which transactions are likely to be fraud. In addition, participants are encouraged 
                        to integrate Large Language Models into their app for further insights.'''),
                html.Img(src='/assets/test.png', className='imagen-clase')
            ]),
            html.Div([
                html.H4('Imbalanced Dataset: Oversampling and Undersampling',id='imbalanced'),
                html.H5('Real  test'),
                html.Img(src='/assets/test.png', className='imagen-clase')
            ]),
            html.Div([
                html.H4('Understanding the Data: type, features, importance and irrelevance',id='dataset'),
                html.H5('Real  test'),
                html.Img(src='/assets/test.png', className='imagen-clase')
            ]),
            html.Div([
                html.H4('Machine Learning Models: Tests, trains and evaluations',id='ml-models'),
                html.H5('Real  test'),
                html.Img(src='/assets/test.png', className='imagen-clase')
            ]),
            html.Div([
                html.H4('Hyperparemeters: relevancy in this case',id='hyperparemeters'),
                html.H5('Real  test'),
                html.Img(src='/assets/test.png', className='imagen-clase')
            ]),
            html.Div([
                html.H4('Results: Interpretation and interesting facts',id='results'),
                html.H5('Real  test'),
                html.Img(src='/assets/test.png', className='imagen-clase')
            ]),
], className="introduction-text")


layout = html.Div([dcc.Location(id="url"), sidebar,html.Hr(className="sidebar-hr"), content ],className="div-home")


