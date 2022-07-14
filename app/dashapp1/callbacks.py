from dash.dependencies import Input
from dash.dependencies import Output
from dash.dependencies import State
from collections import deque
import random
import plotly
import plotly.graph_objs as go

X = deque(maxlen = 20)
X.append(1)

Y = deque(maxlen = 20)
Y.append(1)

def register_callbacks(dashapp):
    @dashapp.callback(
        Output('live-graph', 'figure'),
        [ Input('graph-update', 'n_intervals') ]
    )
    def update_graph_scatter(n):
        X.append(X[-1]+1)
        Y.append(random.randint(1,180))

        data = plotly.graph_objs.Scatter(
                x=list(X),
                y=list(Y),
                name='Scatter',
                mode= 'lines+markers'
        )

        return {
            'data': [data],
            'layout': go.Layout(xaxis=dict(range=[min(X),max(X)]),yaxis = dict(range = [1, 180]),)
        }
