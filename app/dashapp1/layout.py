from dash import dcc
from dash import html

layout = html.Div(
    [
        dcc.Graph(
            id = 'live-graph',
            animate = True,
            animation_options={
                "frame": {
                    "redraw": False,
                },
                "transition": {
                    "duration": 100,
                    "ease": 'linear',
                },
            }
        ),
        dcc.Interval(
            id = 'graph-update',
            interval = 1000,
            n_intervals = 0
        ),
    ]
)