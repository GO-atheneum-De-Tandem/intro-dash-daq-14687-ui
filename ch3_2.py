# Import packages 
from dash import Dash, dcc
import dash_bootstrap_components as dbc

# Initialise the App 
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Create app components
markdown = dcc.Markdown(children='My First app')
slider = dcc.Slider(min=0, max=10, step=1)

# App Layout
app.layout = dbc.Container([
    dbc.Row([
        dbc.Col([
            markdown
        ], width=6),
        
        dbc.Col([
            slider
        ], width=6)
    ])
])


# Run the App 
if __name__ == '__main__':
    app.run(debug=True)