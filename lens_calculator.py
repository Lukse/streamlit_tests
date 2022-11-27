# streamlit run lens.py
# http://localhost:8501/?embed=true


import streamlit as st
import time
import logging as log
import plotly.express as px
import plotly.graph_objects as go
import plotly.figure_factory as ff
from plotly.subplots import make_subplots
import numpy as np
import math

#log.info("Test LOG INFO")
#log.debug("Test LOG DEBUG")
#log.warning("Test LOG WARNING")
#log.error("Test LOG ERROR")


sensors = [
    ['IMX291', 5.63, 3.17],
    ['IMX477', 7.564, 5.476],
    ['AR0330', 4.22, 2.38],
]

hide_streamlit_style = '<style>' + "\n"
hide_streamlit_style = '#MainMenu {visibility: hidden;}' + "\n"
hide_streamlit_style += 'footer {visibility: hidden;}' + "\n"
hide_streamlit_style = '</style>' + "\n"
st.markdown(hide_streamlit_style, unsafe_allow_html=True)


st.title('Lens view angle calculator')
#a = st.sidebar.radio('Select one:', [1, 2])
col1, col2 = st.columns(2)

stripped_sensor_list = []
for s in sensors:
    stripped_sensor_list.append(s[0])
sensor = col1.selectbox(label = 'Select image sensor', options = stripped_sensor_list)

sensor_details = None
for s in sensors:
    if s[0] == sensor:
        sensor_details = s


s_width = sensor_details[1]
s_height = sensor_details[2]
img_circle = round(math.sqrt(math.pow(s_width, 2)  + math.pow(s_height, 2)), 2)


col3, col4, col5, col6, col7, col8 = st.columns(6)
col3.markdown('<font size="5"><span style="color:gray">↔ **'+str(s_width)+'** <font size="2">mm<font></span></font>', unsafe_allow_html=True)
col4.markdown('<font size="5"><span style="color:gray">↕ **'+str(s_height)+'** <font size="2">mm<font></span></font>', unsafe_allow_html=True)
col5.markdown('<font size="5"><span style="color:gray">⤢ **'+str(img_circle)+'** <font size="2">mm<font></span></font>', unsafe_allow_html=True)

focal_length = col2.number_input('Focal length', min_value=1.0, max_value=500.0, value=8.0, step=0.1, format="%2.1f")

angle_h = round((math.atan(s_width / (2 * focal_length)) * 360) / math.pi, 1)
angle_v = round((math.atan(s_height / (2 * focal_length)) * 360) / math.pi, 1)
angle_d = round((math.atan(img_circle / (2 * focal_length)) * 360) / math.pi, 1)

col6.markdown('<font size="5">↔ **'+str(angle_h)+'**°</font>', unsafe_allow_html=True)
col7.markdown('<font size="5">↕ **'+str(angle_v)+'**°</font>', unsafe_allow_html=True)
col8.markdown('<font size="5">⤢ **'+str(angle_d)+'**°</font>', unsafe_allow_html=True)




# https://coolors.co/palettes/trending
fig_d = go.Barpolar(
    r=[4.5],
    theta=[0],
    width=[angle_d],
    marker_color=["#ffbe0b"],
    marker_line_color="black",
    name='Diagonal',
    marker_line_width=0.5,
    opacity=0.8
)

data = [fig_d]


layout = go.Layout(
    polar = dict(
        radialaxis = dict(range=[0, 5], showticklabels=False, griddash='dot', gridcolor='Silver', gridwidth=0.5),
        angularaxis = dict(showticklabels=True, direction="clockwise", rotation=90, gridcolor='Gray', thetaunit = "degrees", dtick = 10, gridwidth=0.3),
        bgcolor='rgba(0,0,0,0.0)',
        #sector = [0-30, 180+30],
        sector = [0, 180],
        
    ),
    legend=dict(
        font=dict(
            size=16
        )
    ),    
    paper_bgcolor='rgba(0,0,0,0)',    
)


config = {'staticPlot': True, 'displaylogo': False, 'displayModeBar': False}

fig = go.Figure(data=data, layout=layout)
fig.update_layout(showlegend=False)
st.plotly_chart(fig, use_container_width=True, config=config)

st.info('Calculations are theoretical. Angles for short focal lenses will be larger due to the gometric distortions and fishye effect.', icon="ℹ️")
st.info('In some modes view angle can be smaller due to image cropping.', icon="ℹ️")
