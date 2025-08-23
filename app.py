# Hello World

# from dash import Dash, html
# app = Dash()
# app.layout = [html.Div("Hello, World!")]
# if __name__ == "__main__":
#     app.run(debug=True)

# # Connecting to data

# # Import packages
# from dash import Dash, html, dash_table
# import pandas as pd
import ssl

# Fix SSL issue
ssl._create_default_https_context = ssl._create_unverified_context

# # Incorporate data
# df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminder2007.csv')

# # Initialize the app
# app = Dash()

# # App layout
# app.layout = [
#     html.Div(children='My First App with Data'),
#     dash_table.DataTable(data=df.to_dict('records'), page_size=10)
# ]

# # Run the app
# if __name__ == '__main__':
#     app.run(debug=True)

# # Visualizing data

# # Import packages
# from dash import Dash, html, dash_table, dcc
# import pandas as pd
# import plotly.express as px

# # Incorporate data
# df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminder2007.csv')

# # Initialize the app
# app = Dash()

# # App layout
# app.layout = [
#     html.Div(children='My First App with Data and a Graph'),
#     dash_table.DataTable(data=df.to_dict('records'), page_size=10),
#     dcc.Graph(figure=px.histogram(df, x='continent', y='lifeExp', histfunc='avg'))
# ]

# # Run the app
# if __name__ == '__main__':
#     app.run(debug=True)


# # Controls and callbacks

# # Import packages
# from dash import Dash, html, dcc, Input, Output, callback, dash_table
# import pandas as pd
# import plotly.express as px
# # Incorporate data
# df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminder2007.csv')
# # Initialize the app
# app = Dash()
# # App layout
# app.layout = [
#   html.Div(children='My First App with Data, Graph, and Controls'),
#   html.Hr(),
#   dcc.RadioItems(options = ['pop', 'lifeExp', 'gdpPercap'], value = 'lifeExp', id = 'controls-and-radio-item'),
#   dash_table.DataTable(data=df.to_dict('records'), page_size=6), 
#   dcc.Graph(figure = {}, id = 'controls-and-graph')
# ]
# # Add control to build the interaction
# @callback(
#     Output(component_id='controls-and-graph', component_property='figure'),
#     Input(component_id='controls-and-radio-item', component_property='value')
# )
# def update_graph(col_chosen):
#   fig = px.histogram(df, x='continent', y=col_chosen, histfunc='avg')
#   return fig
# # Run the app
# if __name__ == '__main__':
#     app.run(debug=True)

# Styling your app (HTML and CSS)

# Import packages
from dash import Dash, html, dash_table, dcc, callback, Output, Input
import pandas as pd
import plotly.express as px
# Incorporate data
df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminder2007.csv')
# Initialize the app - incorporate css
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = Dash(external_stylesheets=external_stylesheets)
# App layout
app.layout = [
    html.Div(className='row', children='My First App with Data, Graph, and Controls',
             style={'textAlign': 'center', 'color': 'blue', 'fontSize': 30}),

    html.Div(className='row', children=[
        dcc.RadioItems(options=['pop', 'lifeExp', 'gdpPercap'],
                       value='lifeExp',
                       inline=True,
                       id='my-radio-buttons-final')
    ]),

    html.Div(className='row', children=[
        html.Div(className='six columns', children=[
            dash_table.DataTable(data=df.to_dict('records'), page_size=11, style_table={'overflowX': 'auto'})
        ]),
        html.Div(className='six columns', children=[
            dcc.Graph(figure={}, id='histo-chart-final')
        ])
    ])
]
# Add controls to build the interaction
@callback(
    Output(component_id='histo-chart-final', component_property='figure'),
    Input(component_id='my-radio-buttons-final', component_property='value')
)
def update_graph(col_chosen):
    fig = px.histogram(df, x='continent', y=col_chosen, histfunc='avg')
    return fig
# Run the app
if __name__ == '__main__':
    app.run(debug=True)
