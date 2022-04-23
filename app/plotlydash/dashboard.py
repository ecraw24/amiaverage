from dash import Dash


def init_dashboard(server):
    """Create a Plotly Dash dashboard."""
    dash_app = dash.Dash(
        server=server,
        routes_pathname_prefix='/graphapp/',
        external_stylesheets=[
            '/static/enterInfo.css',
        ]
    )

    # Create Dash Layout
    dash_app.layout = html.Div(id='dash-container')

    return dash_app.server
