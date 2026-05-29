import pandas as pd
from dash import Dash, dcc, html, Input, Output
import plotly.express as px

url = "https://raw.githubusercontent.com/GO-atheneum-De-Tandem/intro-dash-daq-Pimguin77/refs/heads/master/immigrati_00003_stranieri_seriecittaprovenienza%20(1).csv"
# CSV laden
df = pd.read_csv(
    url,
    sep=";",
    encoding="latin-1"
)

df["Numero Immigrati"] = pd.to_numeric(df["Numero Immigrati"], errors="coerce")
df["Anno"] = pd.to_numeric(df["Anno"], errors="coerce")
df = df.dropna(subset=["Anno", "Numero Immigrati"])
df["Anno"] = df["Anno"].astype(int)

# Pivot
df_pivot = df.pivot_table(
    index="Anno",
    columns="Cittadinanza",
    values="Numero Immigrati",
    aggfunc="sum",
    fill_value=0
)

years = sorted(df_pivot.index.tolist())

max_x = df_pivot.max().max()

app = Dash(__name__)

server = app.server

app.layout = html.Div([
    html.H1("Immigranten per land"),

    dcc.Slider(
        id="year-slider",
        min=min(years),
        max=max(years),
        step=1,
        value=min(years),
        marks={int(y): str(y) for y in years}
    ),
    dcc.Interval(
    id="interval-component",
    interval=1000,  # elke 1 seconde
    n_intervals=0
),

    dcc.Graph(id="bar-chart")
])
from dash.dependencies import State


app.callback(
    Output("year-slider", "value"),
    Input("interval-component", "n_intervals"),
    State("year-slider", "value")
)
def update_slider(n, current_year):
    current_index = years.index(current_year)

    next_index = (current_index + 1) % len(years)

    return years[next_index]
    
def update_graph(year):
    data = df_pivot.loc[year].sort_values(ascending=False).head(10)

    fig = px.bar(
        x=data.values,
        y=data.index,
        orientation='h',
        labels={"x": "Aantal immigranten", "y": "Land"},
        title=f"Aantal immigranten - {year}"
    )

fig.update_layout(
    yaxis={'categoryorder':'total ascending'},
    xaxis=dict(range=[0, max_x])

    return fig

if __name__ == "__main__":
    app.run(debug=True)
