import plotly.graph_objects as go
import plotly.express as px


def plot():
    fig = go.Figure()

    fig.add_trace(go.Line(x=[i for i in range(10)],
                          y=[i*i for i in range(10)]))

    return fig


def plotBar(datapoint, title, xlabel, ylabel):
    fig = go.Figure()

    layout = go.Layout(title=title,
                       xaxis=dict(title=xlabel),
                       yaxis=dict(title=ylabel))
    fig = go.Figure(layout=layout)

    fig.add_trace(go.Bar(x=datapoint.index,
                         y=datapoint.values))

    return fig

def plotLine(datapoint, title, xlabel, ylabel):
    fig = go.Figure()

    layout = go.Layout(title=title,
                       xaxis=dict(title=xlabel),
                       yaxis=dict(title=ylabel))
    fig = go.Figure(layout=layout)

    fig.add_trace(go.Line(x=datapoint.index,
                         y=datapoint.values))

    return fig


def plotBarh(datapoint, title, xlabel, ylabel, orientation="h"):
    fig = go.Figure()

    layout = go.Layout(title=title,
                       xaxis=dict(title=xlabel),
                       yaxis=dict(title=ylabel))
    fig = go.Figure(layout=layout)

    fig.add_trace(go.Bar(x=datapoint.values[::-1],
                         y=datapoint.index[::-1], orientation=orientation))

    return fig


def plotScatter(datapoints, x, y, n, names, title, xlabel, ylabel):
    fig = go.Figure()

    layout = go.Layout(title=title,
                       xaxis=dict(title=xlabel),
                       yaxis=dict(title=ylabel))
    fig = go.Figure(layout=layout)

    for i in range(n):
        fig.add_trace(go.Scatter(x=datapoints[i][x], y=datapoints[i][y],
                                 mode='lines',
                                 name=names[i]))

    return fig



def plotChloropeth(datapoints, title="default title"):

    layout = go.Layout(title=title)

    fig = go.Figure({
        "type": 'choropleth',
        "locations": datapoints.index,
        "locationmode": 'country names',
        "z": datapoints.values},
        layout=layout)

    return fig
