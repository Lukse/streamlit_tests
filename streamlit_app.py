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
#import pandas as pd
from htbuilder import HtmlElement, div, ul, li, br, hr, a, p, img, styles, classes, fonts
from htbuilder.units import percent, px
from htbuilder.funcs import rgba, rgb
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


#st.set_page_config(layout="wide")
st.title('Lens calculator')
#a = st.sidebar.radio('Select one:', [1, 2])
col1, col2 = st.columns(2)

stripped_sensor_list = []
for s in sensors:
    stripped_sensor_list.append(s[0])
sensor = col1.selectbox(label = 'Image sensor', options = stripped_sensor_list)

col3, col4, col5, col6, col7, col8 = st.columns(6)
sensor_details = None
for s in sensors:
    if s[0] == sensor:
        sensor_details = s


s_width = sensor_details[1]
s_height = sensor_details[2]
img_circle = round(math.sqrt(math.pow(s_width, 2)  + math.pow(s_height, 2)), 2)



col3.metric("Horizontal [mm]", s_width, delta=None, delta_color="normal", help=None)
col4.metric("Vertical [mm]", s_height, delta=None, delta_color="normal", help=None)
col5.metric("Image circle [mm]", img_circle, delta=None, delta_color="normal", help=None)
#st.write('You selected:', sensor)






focal_length = col2.number_input('Focal length', min_value=1.0, max_value=500.0, value=8.0, step=0.1, format="%2.1f")
#focal_length = col2.slider('Focal length', min_value=1.0, max_value=500.0, value=8.0, step=0.1, format="%2.1f", help="Lens focal length")
#st.write('You selected:', focal_length)



angle_h = round((math.atan(s_width / (2 * focal_length)) * 360) / math.pi, 1)
angle_v = round((math.atan(s_height / (2 * focal_length)) * 360) / math.pi, 1)
angle_d = round((math.atan(img_circle / (2 * focal_length)) * 360) / math.pi, 1)

col6.metric("HFOV [Â°]", angle_h, delta=None, delta_color="normal", help=None)
col7.metric("VFOV [Â°]", angle_v, delta=None, delta_color="normal", help=None)
col8.metric("DIAG [Â°]", angle_d, delta=None, delta_color="normal", help=None)


#335c67

'''
colors = ['rgba(0x33, 0x5c, 0x67, 0.8)',
          'rgba(111, 231, 219, 0.8)',
          'rgba(184, 87, 82, 0.8)']
'''

'''
colors = ['hsla(1, 100%, 50%, 0.5)',
          'hsla(80, 100%, 50%, 0.5)',
          'hsla(270, 100%, 50%, 0.5)']
'''

colors = ['#01161e',
          '#124559',
          '#598392']



fig = go.Figure(go.Barpolar(
    r=[4.5, 4, 3.5],
    theta=[0, 0.001, 0.002],
    width=[angle_d, angle_h, angle_v],
    marker_color=colors,
    marker_line_color="black",
    marker_line_width=0.5,
    opacity=0.8
))


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

'''
fig.update_layout(
    template=None,
    polar = dict(
        radialaxis = dict(range=[0, 5], showticklabels=False, ticks='', griddash='dot'),
        angularaxis = dict(showticklabels=True, ticks='', direction="clockwise", rotation=90),
    )
)
'''

layout = go.Layout(
    #template=None,
    polar = dict(
        radialaxis = dict(range=[0, 5], showticklabels=False, ticks='', griddash='dot', gridcolor='Silver'),
        angularaxis = dict(showticklabels=True, ticks='', direction="clockwise", rotation=90, gridcolor='Red'),
        bgcolor='rgba(0,0,0,0.0)',

    ),
    legend=dict(
        font=dict(
            size=16
        )
    ),    
    paper_bgcolor='rgba(0,0,0,0)',    
    #paper_bgcolor='rgb(233,233,233)',
    #plot_bgcolor='rgba(100,0,0,0.5)',
    #bgcolor='rgba(100,0,0,0.5)',
    #color='rgba(100,0,0,0.5)',
    #title='View angle',
    #font=dict(
    #    size=16
    #),    
)


# TODO: add exact angles on the graph
# todo: show +/- angle
# remove 90* deg line

#config = {'staticPlot': True, 'displaylogo': False, 'displayModeBar': False}
config = {'staticPlot': True, 'displaylogo': False, 'displayModeBar': False}
#st.plotly_chart(fig, use_container_width=True, config=config)

fig = go.Figure(data=data, layout=layout)
fig.update_layout(showlegend=True)
#fig.update_polars(bgcolor='white')
#fig.update_layout(olot_bgcolor="#FF00FF")
st.plotly_chart(fig, use_container_width=True, config=config)



st.info('Calculations are theoretical. Angles for short focal lenses will be larger due to the gometric distortions and fishye effect.', icon="â„¹ï¸")
st.info('In some modes view angle can be smaller due to image cropping.', icon="â„¹ï¸")









def image(src_as_string, **style):
    return img(src=src_as_string, style=styles(**style))

def link(link, text, **style):
    return a(_href=link, _target="_blank", style=styles(**style))(text)

def layout(*args):
    style = """
    <style>
        MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        .stApp { bottom: 60px; }
    </style>
    """

    style_div = styles(
        position="fixed",
        right=0,
        bottom=0,
        margin=px(0, 15, 0, 0),
        text_align="center",
        opacity=0.5,
    )

    body = p()
    foot = div(
        style=style_div
    )(
        body
    )

    st.markdown(style, unsafe_allow_html=True)
    for arg in args:
        if isinstance(arg, str):
            body(arg)
        elif isinstance(arg, HtmlElement):
            body(arg)
    st.markdown(str(foot), unsafe_allow_html=True)

def footer():
    myargs = [
        link("https://kurokesu.com", image('https://kurokesu.com/home/images/logo/kurokesu_1.png',)),
    ]
    layout(*myargs)


#footer()








'''
    //alert(document.calculatex.first.value);
            var s_width = document.calculate_angles.s_width.value;
            var s_height = document.calculate_angles.s_height.value;
            var s_diag = document.calculate_angles.s_diag.value;
            var lens_mm = document.calculate_angles.lens_mm.value;

            // calculate sensor diag length
            var d = Math.sqrt((s_width * s_width) + (s_height * s_height));
            d = Number((d).toFixed(1));
            document.calculate_angles.s_diag.value = d;

            // calculate view angles
            var angle_h = (Math.atan(s_width / (2 * lens_mm)) * 360) / Math.PI;
            document.calculate_angles.fov_h.value = Number((angle_h).toFixed(1));

            var angle_v = (Math.atan(s_height / (2 * lens_mm)) * 360) / Math.PI;
            document.calculate_angles.fov_v.value = Number((angle_v).toFixed(1));

            var angle_d = (Math.atan(d / (2 * lens_mm)) * 360) / Math.PI;
            document.calculate_angles.fov_d.value = Number((angle_d).toFixed(1));
            
            draw(angle_d);
'''
