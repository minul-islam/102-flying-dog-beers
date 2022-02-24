import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go

########### Define your variables
steps=['Sage Maker', 'Github', 'Python', 'HeroKu']
fun_values=[10, 5, 10, 10]
effort_values=[5, 10, 10, 10]
color1='red'
color2='blue'
mytitle='Learning Fun & Effort'
tabtitle='Learning Topic!'
myheading='Fun & Effort of Learning'
label1='Fun'
label2='Effort'
githublink='https://github.com/austinlasseter/flying-dog-beers'
sourceurl='https://www.flyingdog.com/beers/'

########### Set up the chart
bitterness = go.Bar(
    x=steps,
    y=fun_values,
    name=label1,
    marker={'color':color1}
)
alcohol = go.Bar(
    x=steps,
    y=effort_values,
    name=label2,
    marker={'color':color2}
)

beer_data = [bitterness, alcohol]
beer_layout = go.Layout(
    barmode='group',
    title = mytitle
)

beer_fig = go.Figure(data=beer_data, layout=beer_layout)


########### Initiate the app
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server
app.title=tabtitle

########### Set up the layout
app.layout = html.Div(children=[
    html.H1(myheading),
    dcc.Graph(
        id='flyingdog',
        figure=beer_fig
    ),
    html.A('Code on Github', href=githublink),
    html.Br(),
    html.A('Data Source', href=sourceurl),
    ]
)

if __name__ == '__main__':
    app.run_server()
