import dash
from dash import html

dash.register_page(__name__, path='/')

layout = html.Div([
    html.H2('Home'),
    html.Div('This is our Home page content. Here I\'ll explain more about this Dash'),
    
])
