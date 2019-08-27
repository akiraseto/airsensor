# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go

from database import db_session
from models import Data
import datetime
from dateutil.relativedelta import relativedelta

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

data_week = []
data_month = []
data_all = []

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
app.title = 'Air Condition'

# apache2起動で必要
server = app.server

app.layout = html.Div(children=[
    html.H2(children='airsensor 家の空気環境'),
    html.Div(children=[
        dcc.RadioItems(
            id = 'radiobutton',
            options=[
                {'label': 'week', 'value': 'week'},
                {'label': 'month', 'value': 'month'},
                {'label': 'all', 'value': 'all'},
            ],
            value='week',
            labelStyle = {'display': 'inline-block', 'margin-left':'15px', 'margin-bottom':'5px'},
        ),
    ]),

    html.Div(className='row',id='grapharea')
], style={'textAlign': 'center'})

@app.callback(
    dash.dependencies.Output('grapharea', 'children'),
    [dash.dependencies.Input('radiobutton', 'value')]
)

def update_graph(factor):
    data = []
    dates = []
    temp = []
    humi = []
    co2 = []
    tvoc = []
    press = []

    if factor == 'week':
        global data_week
        before_day = datetime.datetime.now() - datetime.timedelta(days = 7)

        if len(data_week) < 1:
            data = db_session.query(Data.date, Data.temp, Data.humi, Data.di, Data.co2, Data.tvoc, Data.press, Data.alti, Data.sea, Data.id).filter(Data.date >= before_day).all()
        else:
            data = data_week

    elif factor == 'month':
        global data_month
        before_day = datetime.datetime.now() - relativedelta(months=1)

        if len(data_month) < 1:
            data = db_session.query(Data.date, Data.temp, Data.humi, Data.di, Data.co2, Data.tvoc, Data.press, Data.alti, Data.sea, Data.id).filter(Data.date >= before_day).all()
        else:
            data = data_month

    elif factor == 'all':
        if len(data_all) < 1:
            data = db_session.query(Data.date, Data.temp, Data.humi, Data.di, Data.co2, Data.tvoc, Data.press, Data.alti, Data.sea, Data.id).all()
        else:
            data = data_all

    for datum in data:
        dates.append(datum.date)
        temp.append(datum.temp)
        humi.append(datum.humi)
        co2.append(datum.co2)
        tvoc.append(datum.tvoc)
        press.append(datum.press)

    return [
        html.Div(className='six columns', children=[
            html.Div(children=dcc.Graph(
                id='left-graph',
                figure={
                    'data':[
                        go.Scatter(
                            x=dates,
                            y=temp,
                            mode='lines+markers',
                            name='温度',
                            opacity=0.7,
                            yaxis='y1'
                        ),
                        go.Scatter(
                            x=dates,
                            y=humi,
                            mode='lines+markers',
                            name='湿度',
                            yaxis='y2'
                        )
                    ],
                    'layout': go.Layout(
                        height=800,
                        title='気温&湿度',
                        xaxis=dict(title='日時'),
                        yaxis=dict(title='温度',side='left', showgrid=True, range=[min(temp)-5, max(temp)+5]),
                        yaxis2=dict(title='湿度',side='right',overlaying='y', showgrid=False, range=[min(humi)-5, max(humi)+5]),
                        margin=dict(l=60, r=50, b=50, t=50),
                        legend={'x': 0.03, 'y': 1}
                    )
                }
            ))
        ]),

        html.Div(className='six columns',children=html.Div([
                dcc.Graph(
                    id='right-top-graph',
                    figure={
                        'data':[
                            go.Scatter(
                                x=dates,
                                y=co2,
                                mode='lines+markers',
                                name='CO2濃度',
                                opacity=0.7,
                                yaxis='y1'
                            ),
                            go.Scatter(
                                x=dates,
                                y=tvoc,
                                mode='lines+markers',
                                name='空気の汚れ',
                                yaxis='y2'
                            )
                        ],
                        'layout': go.Layout(
                            height=400,
                            title='CO2濃度と空気の汚れ',
                            xaxis=dict(title='日時'),
                            yaxis=dict(title='CO2濃度',side='left', showgrid=True, range=[min(co2)-100, 2000]),
                            yaxis2=dict(title='空気の汚れ',side='right',overlaying='y', showgrid=False, range=[min(tvoc)-100, 1000]),
                            margin=dict(l=50, r=60, b=50, t=50),
                            legend={'x': 0.03, 'y': 1}
                        ),
                    }
                ),

                dcc.Graph(
                    id='right-bottom-graph',
                    figure={
                        'data':[
                            go.Scatter(
                                x=dates,
                                y=press,
                                mode='lines+markers',
                                name='気圧',
                                opacity=0.7,
                                yaxis='y1'
                            ),
                        ],
                        'layout': go.Layout(
                            height=400,
                            title='気圧',
                            xaxis=dict(title='日時'),
                            yaxis=dict(title='気圧',side='left', showgrid=True, range=[min(press)-5, max(press)+5]),
                            margin=dict(l=50, r=60, b=50, t=50),
                            legend={'x': 0.03, 'y': 1}
                        ),
                    }
                )
            ],))
    ]
