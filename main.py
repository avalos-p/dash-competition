from dash import Dash, html
from dash_bootstrap_components.themes import CYBORG
from src.components.layout import create_layout


def main() -> None:

    app = Dash(external_stylesheets=[CYBORG])
    app.title = "Credit Card transactions fraud detection 💳🕵️ " 
    app.layout = create_layout(app)
    app.run()


if __name__ == "__main__":
    main()

'''
# To do: probably I can explain more about the project. 
# Another plot using original dataset
# Mltiple pages option

'''
