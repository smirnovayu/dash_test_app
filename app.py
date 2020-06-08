# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

import pandas as pd
df = pd.read_csv('voting_data_eng.csv')

names = list(set(df['region_name']))
names.sort()

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

server = app.server

app.layout = html.Div([
        
    html.Div([
        dcc.Dropdown(
            id='dropdown_test',
            options=[{'label':name, 'value':name} for name in names],
            #value = names
            value = 'Respublika Kalmykia'
            ),
            ],style={'width': '20%', 'display': 'inline-block'}),
                
    dcc.Graph(id='graph-with-dropdown'),
                
  dcc.Graph(
        id='life-exp-vs-gdp',
        figure={
            'data': [
                dict(
                    x=df[df['region_name'] == 'Altajskij kraj']['Putin Vladimir Vladimirovich'],
                    y=df[df['region_name'] == 'Altajskij kraj']['Grudinin Pavel Nikolaevich'],
                    text=df[df['region_name'] == 'Altajskij kraj']['subregion_name'],
                    mode='markers',
                    opacity=0.7,
                    marker={
                        'size': 15,
                        'line': {'width': 0.5, 'color': 'white'}
                    }
                ) #for i in df.region_name.unique()
            ],
            'layout': dict(
                xaxis={'type': 'log', 'title': 'GDP Per Capita'},
                yaxis={'title': 'Life Expectancy'},
                margin={'l': 40, 'b': 40, 't': 10, 'r': 10},
                legend={'x': 0, 'y': 1},
                hovermode='closest'
            )
        }
    )
                
], style={'columnCount': 1})
            
            
@app.callback(
    Output('graph-with-dropdown', 'figure'),
    [Input('dropdown_test', 'value')])
def update_figure(selected_region):
    filtered_df = df[df.region_name == selected_region]
    traces = []
    traces.append(dict(
            x=filtered_df['Putin Vladimir Vladimirovich'],
            y=filtered_df['Grudinin Pavel Nikolaevich'],
            text=filtered_df['subregion_name'],
            mode='markers',
            opacity=0.7,
            marker={
                    'size': 15,
                    'line': {'width': 0.5, 'color': 'white'}
                    }
            ))
    return {
        'data': traces,
        'layout': dict(
            xaxis={'type': 'log', 'title': 'GDP Per Capita'},
            yaxis={'title': 'Life Expectancy'},
            margin={'l': 40, 'b': 40, 't': 10, 'r': 10},
            legend={'x': 0, 'y': 1},
            hovermode='closest',
            # transition = {'duration': 500},
        )
    }            
            

if __name__ == '__main__':
    app.run_server(debug=True)
    
    
    
    
