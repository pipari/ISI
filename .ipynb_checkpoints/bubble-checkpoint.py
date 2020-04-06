import plotly.io as pio
#pio.renderers.default = "iframe"

import plotly.express as px
import pandas as pd
import plotly.graph_objects as go
import chart_studio.plotly as py
import chart_studio

dataframe_bubble = pd.read_csv("data/graph_table.csv", sep=";", decimal=",")
username = 'jaemikew' 
api_key = '3DMC84ZXuI11xkaPDFt3'

chart_studio.tools.set_credentials_file(username=username, api_key=api_key)

def generate_bubbles(w, h):
fig = px.scatter(dataframe_bubble, 
                x="Intergenerational Solidarity Index", 
                y="v2x_libdem", 
                size="Population", 
                color="Region",
                hover_name="Country", 
                size_max=60,
                )
fig.add_trace(go.Scatter
            (x=['0', '100']
            , y=[0.42, 0.42]
            , mode="lines"
            , name=""))
fig.add_trace(go.Scatter
            (x=['50', '50']
            , y=[-0.1, 1]
            , mode="lines"
            , name=""))
fig.update_traces(line_color='#456987')
    
    fig.update_layout(showlegend=False,
                    width = w,
                    height = h,
                    margin=dict(
            l=0,
            r=0,
            b=0,
            t=0,
            pad=0
                    ),
                    autosize=False,
                    plot_bgcolor="#eeeeee",
                    yaxis = dict(
                    scaleanchor = "x",
                    scaleratio = 119,)#scale ratio usually something different
                    )
    fig.update_xaxes(showgrid=False,
                    zeroline=False,
                    range=[0, 100],
                    showticklabels=True,
                    )
    fig.update_yaxes(title_text='vDem Liberal Democracy',
                    showgrid=False,
                    zeroline=False,
                    range=[0, 0.88], #remember to change this for other indexes
                    showticklabels=True,)
    return fig

configurations = [
    {"name": "Smurf1", "w": 500, "h": 500},
    {"name": "Smurf2", "w": 200, "h": 20},
    {"name": "Smurf3", "w": 5400, "h": 5400},
    {"name": "Smurf4", "w": 600, "h": 600},
]

for item in configurations:
    fig = generate_bubbles(w=item["w"], h=item["h"])
    fig.show()
    py.plot(fig, filename = item["name"], auto_open=False)