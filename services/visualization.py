import plotly.express as px

def create_chart(df, chart_type, x, y):

    if chart_type == "Bar":
        fig = px.bar(df, x=x, y=y)
    elif chart_type == "Line":
        fig = px.line(df, x=x, y=y)
    elif chart_type == "Scatter":
        fig = px.scatter(df, x=x, y=y)
    else:
        fig = px.histogram(df, x=x)

    fig.update_layout(template="plotly_dark")
    return fig
