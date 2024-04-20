import dash
from dash import html, dcc, callback
from dash.dependencies import Input, Output

from utils.get_data import models_dict
from utils.styles import selected_tab, not_selected_tab,dropdown_mystyle

import plotly.express as px
from plotly.subplots import make_subplots
import numpy as np

dash.register_page(__name__,name="Model Comparision")

models_information = models_dict() 

models_order = sorted(models_information.items(), key=lambda x: x[1]['accuracy'],
                       reverse=True) # Ordering data by accyracty
models_names = [nombre for nombre, datos in models_order]
models_data_order = [(nombre, datos['accuracy'], datos['conf_matrix'], datos['info']) for nombre, datos in models_order]



layout = html.Div([
    html.Div(children=[
            html.H2("Models:"),
            dcc.Dropdown(
                id='id-models-dropdown',
                className='models-dropdown',
                options=[{"label": name, "value": name} for name in models_names],
                value=[],
                multi=True,
                style=dropdown_mystyle
            ),
            html.Button(
                className="dropdown-button",
                children=[html.Strong("Select All")],
                id='id-select-all-models-button',
                n_clicks=0,
            ),
        ]),    
    html.Div(dcc.Tabs(id="tabs-graphs",
        className="custom-tabs", children=[
        dcc.Tab(label='Comparition', id='id-chart',style = not_selected_tab, selected_style=selected_tab),
        dcc.Tab(label='Models Explanation', id='id-information',style =not_selected_tab, selected_style = selected_tab),
        ])
        ),
])

@callback(
    Output('id-models-dropdown', "value"),
    Input('id-select-all-models-button', "n_clicks"))
def select_all_models(n_clicks):
    return models_names


@callback(
    [Output('id-chart', 'children'),
     Output('id-information','children')],

    [Input('id-models-dropdown', "value")]
    )

def update_chart(selected_models: list[str]) -> html.Div:
    filtered_data = [(nombre, round(accuracy * 100, 2), conf_matrix, model_info) for nombre, accuracy, conf_matrix, model_info in models_data_order if nombre in selected_models]
    num_selected_models = len(filtered_data)

    if num_selected_models == 1:
        model, accuracy, matrix, model_info = filtered_data[0]

        matrix = np.flipud(matrix)
        fig_matrix = px.imshow(matrix,
                    labels=dict(x="Predicted label", y="True label"),
                    y=['True 1','False 0'],
                    x=['Predicted False 0', 'Predicted True 1'],
                    color_continuous_scale=["#DFEBEB", "#9EA1D4"],
                    text_auto=True) 
        fig_matrix.update_layout(title=model + ' - Confusion Matrix ',
                         xaxis_title='Predicted',
                         yaxis_title='True',
                         coloraxis_showscale=False,
                         paper_bgcolor='rgba(0,0,0,0)',
                         font_color="white")
            
        fig_pie = px.pie(names=[f"{model} 🎯", 'Discrepancy ❌'], values=[accuracy, 100-accuracy],
                 color_discrete_sequence=["#9EA1D4","#DFEBEB"], title="Model Accuracy (%) : " + model)
        fig_pie.update_layout(paper_bgcolor='rgba(0,0,0,0)',font_color="white")
        

        graph_div = html.Div([
            html.Div(dcc.Graph(figure=fig_matrix), style={'display': 'inline-block', 'width': '49%'}),
            html.Div(dcc.Graph(figure=fig_pie), style={'display': 'inline-block', 'width': '49%'})
            ], id='id-chart', className='graph-container1')       
                
        information_div = html.Div([html.H2("About the model"),html.H4(model),
                                     html.P(model_info)],id='id-information',className='info-container')  

        return graph_div, information_div

    elif num_selected_models == 0:
        no_data_div = html.Div([html.H5("No data selected.")], id='id-chart',style ={'color':'white'})
        no_info_div = html.Div([html.H5("No data selected.")],id='id-information',style ={'color':'white'})
        return no_data_div, no_info_div 
    
    else:
        filtered_data.sort(key=lambda x: x[1])  # Order by accuracy

        
        # models = [entry[0] for entry in filtered_data]
        # accuracies = [entry[1] for entry in filtered_data]
        models, accuracies, coef_matrices, models_info = zip(*[(entry[0], entry[1], entry[2], entry[3]) for entry in filtered_data])


        fig = px.bar(x=accuracies, y=models, orientation='h',
                         labels={'x': 'Accuracy (%)', 'y': 'Model '},
                         title='Accuracy Comparison 🎯')
            
        fig.update_layout(
            title_font_size=24,  # Adjust the font size of the title
            title_x=0,  # Adjust the title to the left
            template="seaborn",
            paper_bgcolor='rgba(0,0,0,0)',font_color="white") #this template is working
        fig.update_traces(marker=dict(color=accuracies, 
                               colorscale='spectral', 
                               cmin=min(accuracies), 
                               cmax=max(accuracies)))
        for i, acc in enumerate(accuracies):
            fig.add_annotation(x=acc, y=models[i], text=str(acc)+'%', showarrow=False, font=dict(color='black', size=11))
            
        graph_div = html.Div(dcc.Graph(figure=fig), id='id-chart',className='graph-container2')
        
        
        model_info_divs = [html.Div([html.H4(models[i]),html.P(models_info[i])]) for i in range(len(models))]
        model_info_divs = model_info_divs[::-1]

        information_div = html.Div([
            html.H2("Explaining models"),
            html.Div(model_info_divs, id='model-info-list')], id='id-information',className='info-container')

        return graph_div, information_div