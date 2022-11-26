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

