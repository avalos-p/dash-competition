import plotly.express as px
from plotly.subplots import make_subplots

from dash import Dash, dcc, html
from dash.dependencies import Input, Output

from . import ids 
import json
import numpy as np

'''
Importing data
'''
with open('data/modelos_dic.json', 'r') as json_file:
    models_dict = json.load(json_file)

# Ordering by accuracy
models_order = sorted(models_dict.items(), key=lambda x: x[1]['accuracy'], reverse=True)
MODELS_DATA = [(nombre, datos['accuracy'], datos['conf_matrix']) for nombre, datos in models_order]


'''
Generates comparison plots between models.

If only one model is chosen, the resulting confusion matrix of the model's test will be displayed
as a pie chart of accuracy and error.

On the other hand, if more than one model is selected, a comparison is made between them.

And if no model is chosen, a notification is displayed indicating that none has been selected.

'''

def render(app: Dash) -> html.Div:
    @app.callback(
        Output(ids.PERCENTAGE_CHART, "children"),
        [
            Input(ids.MODELS_DROPDOWN, "value"),
        ],
    )

    def update_chart(selected_models: list[str]) -> html.Div:
        filtered_data = [(nombre, round(accuracy * 100, 2), conf_matrix) for nombre, accuracy, conf_matrix in MODELS_DATA if nombre in selected_models]
        num_selected_models = len(filtered_data)

        if num_selected_models == 1:
            model, accuracy, matrix = filtered_data[0]

            matrix = np.flipud(matrix)

            fig_matrix = px.imshow(matrix,
                       labels=dict(x="Predicted label", y="True label"),
                       y=['True 1','False 0'],
                       x=['Predicted False 0', 'Predicted True 1'],
                       template="seaborn",
                       text_auto=True,
                       color_continuous_scale='Viridis') 
            
            fig_matrix.update_layout(title=model + ' - Confusion Matrix ',
                         xaxis_title='Predicted',
                         yaxis_title='True',
                         template="seaborn",
                         coloraxis_showscale=False)
            
            fig_pie = px.pie(names=[f"{model} 🎯", 'Discrepancy ❌'], values=[accuracy, 100-accuracy], template="seaborn",
                 title="Model Accuracy (%) : " + model,
                 color_discrete_sequence=px.colors.sequential.Viridis) 
            
            fig = make_subplots(rows=1, cols=2, specs=[[{'type': 'xy'}, {'type': 'domain'}]])

            fig.add_trace(fig_matrix.data[0], row=1, col=1)
            fig.add_trace(fig_pie.data[0], row=1, col=2)

            fig.update_layout(title=f"Model Evaluation: Confusion Matrix 📊 and Accuracy 🎯 <br><sup> <b>{model}</b> </sup>",
                              title_font_size=24,
                              title_x=0,
                              template="seaborn", coloraxis_showscale=False) #this template is working

            return html.Div(dcc.Graph(figure=fig), id=ids.PERCENTAGE_CHART)
        


        elif num_selected_models == 0:
            return html.Div("No data selected. 🕸", id=ids.PERCENTAGE_CHART)

        else:
            filtered_data.sort(key=lambda x: x[1])  # Order by accuracy

            models = [entry[0] for entry in filtered_data]
            accuracies = [entry[1] for entry in filtered_data]
            fig = px.bar(x=accuracies, y=models, orientation='h',
                         labels={'x': 'Accuracy (%)', 'y': 'Model '},
                         title='Accuracy Comparison 🎯'
                         )
            
            fig.update_layout(
                title_font_size=24,  # Adjust the font size of the title
                title_x=0,  # Adjust the title to the left
                template="seaborn" 
                ) #this template is working
            fig.update_traces(marker=dict(color=accuracies, 
                               colorscale='spectral', 
                               cmin=min(accuracies), 
                               cmax=max(accuracies)))
            for i, acc in enumerate(accuracies):
                fig.add_annotation(x=acc, y=models[i], text=str(acc)+'%', showarrow=False, font=dict(color='black', size=11))
            return html.Div(dcc.Graph(figure=fig), id=ids.PERCENTAGE_CHART)
    
    return html.Div(id=ids.PERCENTAGE_CHART)
