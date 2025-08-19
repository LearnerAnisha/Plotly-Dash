# Hello World

# from dash import Dash, html
# app = Dash()
# app.layout = [html.Div("Hello, World!")]
# if __name__ == "__main__":
#     app.run(debug=True)

# Connecting to data

# Import packages
from dash import Dash, html, dash_table
import pandas as pd
import ssl

# Fix SSL issue
ssl._create_default_https_context = ssl._create_unverified_context

# Incorporate data
df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminder2007.csv')

# Initialize the app
app = Dash()

# App layout
app.layout = [
    html.Div(children='My First App with Data'),
    dash_table.DataTable(data=df.to_dict('records'), page_size=10)
]

# Run the app
if __name__ == '__main__':
    app.run(debug=True)

