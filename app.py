from dash import Dash, dcc, html, Input, Output
import plotly.express as px

import numpy as np
import pandas as pd



app = Dash(__name__)

app.layout = html.Div([
    dcc.Graph(id='graph-with-slider'),
    dcc.Slider(
        0,
        250,
        value=5,
        id='nsize-slider'
    )
])


@app.callback(
    Output('graph-with-slider', 'figure'),
    Input('nsize-slider', 'value'))
def update_figure(selected_nsize):

    fav_score_samples = []
    for _ in range(100):
        values = [1, 2, 3, 4, 5]
        probs = [0.1, 0.1, 0.1, 0.4, 0.3]
        sample = np.random.choice(values, selected_nsize, p=probs)
        fav_score = (sample > 3).mean()
        fav_score_samples.append(fav_score)

    fig = px.histogram(fav_score_samples)

    fig.update_layout(transition_duration=500, xaxis=dict(range=[0, 1], autorange=False))

    return fig


if __name__ == '__main__':
    app.run_server(debug=True)
