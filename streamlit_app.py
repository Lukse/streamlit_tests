# streamlit run lens.py  --menu-for-production
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



log.info("Test LOG INFO")
log.debug("Test LOG DEBUG")
log.warning("Test LOG WARNING")
log.error("Test LOG ERROR")



#hide_streamlit_style = '<style>' + "\n"
#hide_streamlit_style = '#MainMenu {visibility: hidden;}' + "\n"
#hide_streamlit_style += 'footer {visibility: hidden;}' + "\n"
#hide_streamlit_style = '</style>' + "\n"
#st.markdown(hide_streamlit_style, unsafe_allow_html=True)


#st.set_page_config(layout="wide")
st.title('Lens calculator')
#a = st.sidebar.radio('Select one:', [1, 2])
col1, col2 = st.columns(2)


sensor = col1.selectbox(label = 'Select sensor size', 
                      options = ['IMX290', 'AR0330', 'IMX477'])
#st.write('You selected:', sensor)


focal_length = col2.number_input('Focal length', min_value=1.0, max_value=500.0, value=8.0, step=0.1, format="%2.1f", help="Lens focal length")
#focal_length = col2.slider('Focal length', min_value=1.0, max_value=500.0, value=8.0, step=0.1, format="%2.1f", help="Lens focal length")

#st.write('You selected:', focal_length)




'''

x1 = np.random.randn(int(focal_length*100)) - 2
x2 = np.random.randn(200)
x3 = np.random.randn(200) + 2

# Group data together
hist_data = [x1, x2, x3]

group_labels = ['Group 1', 'Group 2', 'Group 3']

# Create distplot with custom bin_size
fig = ff.create_distplot(
        hist_data, group_labels, bin_size=[.1, .25, .5])

# Plot!
st.plotly_chart(fig, use_container_width=True)
'''


'''

my_bar = st.progress(0)
for percent_complete in range(100):
    time.sleep(0.1)
    my_bar.progress(percent_complete + 1)
'''



#layout = go.Layout(
#    showlegend = False,
#)

fig = go.Figure(go.Barpolar(
    r=[4.5],
    theta=[0],
    width=[focal_length*5],
    marker_color=["#E4FF87"],
    marker_line_color="black",
    marker_line_width=0.5,
    opacity=0.8,
))

fig.update_layout(
    template=None,
    polar = dict(
        radialaxis = dict(range=[0, 5], showticklabels=False, ticks='', griddash='dash'),
        angularaxis = dict(showticklabels=True, ticks='', direction="clockwise", rotation=90),
    )
)

# todo: show +/- angle

#config = {'staticPlot': True, 'displaylogo': False, 'displayModeBar': False}
config = {'staticPlot': True, 'displaylogo': False, 'displayModeBar': False}
st.plotly_chart(fig, use_container_width=True, config=config)



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

