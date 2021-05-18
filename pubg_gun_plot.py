import plotly.graph_objects as go
import plotly.offline as pyo


categories = ['Power', 'Rate of Fire', 'Range', 'Capacity', 'Stability']
categories = [*categories, categories[0]]

Groza = [45, 67, 60, 30, 63]
AUG_A3 = [41, 58, 56, 30, 64]
M416 = [41, 75, 56, 30, 63]
AKM = [48, 61, 60, 30, 61]
M24 = [79, 5, 86, 5, 62]

Groza = [*Groza, Groza[0]]
AUG_A3 = [*AUG_A3, AUG_A3[0]]
M416 = [*M416, M416[0]]
AKM = [*AKM, AKM[0]]
M24 = [*M24, M24[0]]


fig = go.Figure(
    data=[
        go.Scatterpolar(r=Groza, theta=categories, fill='toself', name='Groza'),
        go.Scatterpolar(r=AUG_A3, theta=categories, fill='toself', name='AUG A3'),
        go.Scatterpolar(r=M416, theta=categories, fill='toself', name='M416'),
        go.Scatterpolar(r=AKM, theta=categories, fill='toself', name='AKM'),
        go.Scatterpolar(r=M24, theta=categories, fill='toself', name='M24')
    ],
    layout=go.Layout(
        title=go.layout.Title(text='Gun comparison'),
        polar={'radialaxis': {'visible': True}},
        showlegend=True
    )
)

pyo.plot(fig)