import dash
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash()

app.layout = html.Div(children=[
    #here are the HTML elements
    #for the dashboard
    html.H1(children='Hello Dash'),

    html.Div(children='''
        Dash: A web application framework for Python.
    '''),
    #in this basic example, we are manually inputting the data to to graph
    #note how we call the type of the graph
    dcc.Graph(
        id='example-graph',
        figure={
            'data': [
                {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'SF'},
                {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': u'Montréal'},
            ],
            #within the graph we have a layout element
            'layout': {
                'title': 'Dash Data Visualization'
            }
        }
    )
])

#runs the application
if __name__ == '__main__':
    app.run_server(debug=True)