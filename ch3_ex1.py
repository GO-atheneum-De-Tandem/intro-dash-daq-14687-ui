# Import packages
from dash import Dash, html, dcc
import dash_bootstrap_components as dbc

# Initialise the App
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Create app components

dropdown1 = dcc.Dropdown(
    options=[
        {'label': 'CA', 'value': 'CA'},
        {'label': 'FL', 'value': 'FL'},
        {'label': 'DC', 'value': 'DC'}
    ], value='DC'
)
markdown = dcc.Markdown(children='Please select a state')
markdownTitle = dcc.Markdown(children='My New app', style={'textAlign': 'center'})

# App Layout
app.layout = dbc.Container([
    dbc.Row([
        dbc.Col([
        markdownTitle
        ], width=12 ), 
    ]),
    dbc.Row([
        dbc.Col([
            markdown
        ], width=4),
        dbc.Col([
            dropdown1
        ], width=8)
    ])
])

# Run the App
if __name__ == '__main__':
    app.run(debug=True)
