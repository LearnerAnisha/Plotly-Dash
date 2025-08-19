from dash import Dash, html

app = Dash()

app.layout = [html.Div("Hello, World!")]

if __name__ == "__main__":
    app.run(debug=True)
