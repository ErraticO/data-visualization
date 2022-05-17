import plotly as py
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import plotly.graph_objects as go
from jupyter_dash import JupyterDash
import pandas as pd
import numpy as np

py.offline.init_notebook_mode(connected=True)

app = JupyterDash('SimpleExample')
app.layout = html.Div([
    dcc.Dropdown(id='dropdown', options=[
        {'label': 'W', 'value': 'W'},
        {'label': 'exit', 'value': 'exit'}],
                 value='exit'),
    dcc.Graph(id='graph-court')

])


def random_data():
    # sample dataframe of a wide format
    np.random.seed(4)
    cols = list('xyz')
    X = np.random.randint(50, size=(3, len(cols)))
    df = pd.DataFrame(X, columns=cols)
    df.iloc[0] = 0
    return df


df = random_data()


def create_figure(df):
    fig = go.Figure(data=[go.Scatter3d(x=df['x'], y=df['y'], z=df['z'], mode='markers', marker=dict(
        size=10,
        color=df['y'],
        colorscale='Viridis',
        opacity=0.3
    ))])

    # Column max and mins for plotting:
    xmax = df.max(axis=0)['x']
    xmin = df.min(axis=0)['x']
    ymax = df.max(axis=0)['y']
    ymin = df.min(axis=0)['y']
    zmax = df.max(axis=0)['z']
    zmin = df.min(axis=0)['z']

    fig.update_layout(
        scene=dict(xaxis=dict(nticks=4, range=[xmin, xmax], ),
                   yaxis=dict(nticks=4, range=[ymin, ymax], ),
                   zaxis=dict(nticks=4, range=[zmin, zmax], ), ))
    fig = go.FigureWidget(fig)
    return fig

# ploy
fig = create_figure(df)
@app.callback(Output('graph-court', 'figure'),
              [Input('dropdown', 'value')])
def update_figure(selected_value):
    selected_value = selected_value.lower()  # Convert input to "lowercase"
    if selected_value == 'exit':
        print("Good bye.")
        new_x, new_y, new_z = [], [], []
    else:
        print("W, moving forward")
        # new data
        new_x, new_y, new_z = np.random.randint(10, size=(3, 1))

    # update ploy
    fig.add_trace(go.Scatter3d(x=new_x, y=new_y, z=new_z, marker=dict(size=10, color='green'), mode='markers'))

    return fig


app.run_server(debug=False, use_reloader=False)
