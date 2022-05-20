# Task 6 : Test Automation
"""
This  Dash application  will enable Soul Foods to dig into region-specific sales data for Pink Morsels.
"""
from dash import Dash, dcc, html, Input, Output
import plotly.express as px
import pandas as pd
import numpy as np

daily_sales_data = pd.read_csv('E:/Forage/Quantium/Task1/quantium-starter-repo/task_2_data_processing/merged_daily_sales_data.csv', parse_dates=['date'])
daily_sales_data.sort_values(by="date")

app = Dash(__name__)

colors = {
    'background': '#111111',
    'text': '#7FDBFF',
    'title': '#ffeb88'
}

visualization = dcc.Graph(id='graph-with-radio-button')

# create the header
header = html.H1(
    "Pink Morsel Visualizer",
    id="header",
    style={'color': colors['title']}
)

# region picker
region_picker = dcc.RadioItems(
    np.insert(daily_sales_data['region'].unique(), 0, 'all'),
    daily_sales_data['region'].unique()[0],
    id='sales-region-picker',
    inline=True
)

region_picker_wrapper = html.Div(
    [
        html.P('Select Sales Region'),
        region_picker
    ],
    style={
        "font-size": "115%"
    }
)

line_separator = html.Hr(style={'width': '200%',
                                'color': colors['text'],
                                'width': 'inherit'}
                         )

app.layout = html.Div([
    header,
    line_separator,
    region_picker_wrapper,
    line_separator,
    visualization

],
    style={'background': colors['background'],
           'color': colors['text'],
           "textAlign": "center",
           }
)


@app.callback(
    Output('graph-with-radio-button', 'figure'),
    Input('sales-region-picker', 'value'))
def update_figure(selected_region):
    filtered_daily_sales_data = daily_sales_data
    if selected_region != 'all':
        filtered_daily_sales_data = daily_sales_data[daily_sales_data.region == selected_region]
    else:
        pass

    fig = px.line(x=filtered_daily_sales_data["date"],
                  y=filtered_daily_sales_data["sales"],
                  labels={'x': 'Date', 'y': 'Sales'},
                  title='Daily Sales of Pink Morsels')

    fig.update_layout(plot_bgcolor=colors['background'],
                      paper_bgcolor=colors['background'],
                      font_color=colors['text'],
                      transition_duration=500)

    return fig


""""""

if __name__ == '__main__':
    app.run_server(debug=True)
