from dash import Dash, html
from dash_bootstrap_components.themes import CYBORG
from src.components.layout import create_layout


def main() -> None:

    app = Dash(external_stylesheets=[CYBORG])
    app.title = "Credit card fraud detection dashboard"
    app.layout = create_layout(app)
    app.run()


if __name__ == "__main__":
    main()