# Task 3 : Create a Dash Application
"""
The purpose of this Dash app is to answer Soul Foods’s question: “Were sales higher before or after the Pink Morsel price increase on the 15th of January, 2021?”
"""

from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

app = Dash(__name__)

daily_sales_data = pd.read_csv('../task_2_data_processing/merged_daily_sales_data.csv', parse_dates=['date'])
daily_sales_data.sort_values(by="date")

fig = px.line(x=daily_sales_data["date"], y=daily_sales_data["sales"], labels={'x': 'Date', 'y': 'Sales'},
              title='Daily Sales of Pink Morsels')

app.layout = html.Div(children=[
    html.H1(children='Task 3 Dash Application'),

    html.Div(children='''
        The goal of the chart is to answer Soul Foods’s question: “Were daily sales higher before or after the Pink Morsel price increase on the 15th of January, 2021?”
    '''),

    dcc.Graph(
        id='example-graph',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
