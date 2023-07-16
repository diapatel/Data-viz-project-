import streamlit as st
import plotly.express as px
import numpy as np
import pandas as pd

st.set_page_config(layout='wide')
data= pd.read_csv('./india.csv')
list_of_states = list(data['State'].unique())
list_of_states.insert(0,'Overall India')

st.sidebar.title('Visualizing India')
selected_state= st.sidebar.selectbox('Select a state', list_of_states)
primary = st.sidebar.selectbox('Select a primary parameter', sorted(data.columns[5:]))
secondary = st.sidebar.selectbox('Select a secondary parameter', sorted(data.columns[5:]))

plot = st.sidebar.button('Plot a graph')

if plot:
    st.text('Size of the bubble represents primary parameter')
    st.text('Color of the bubble represents secondary parameter')
    if selected_state == 'Overall India':
        #map for india
        fig = px.scatter_mapbox(data, lat='Latitude', lon='Longitude', size=primary, color=secondary,
                                size_max=35, height=600, width=1000,
                                zoom=4, mapbox_style='carto-positron', hover_name='District'
                                )
        st.plotly_chart(fig, size_container_width=True)
    else:
        # map for the state
        state_df = data[data['State'] == selected_state]
        fig = px.scatter_mapbox(state_df, lat='Latitude', lon='Longitude', size=primary, color=secondary,
                                size_max=35, height=600, width=1000,
                                zoom=5, mapbox_style='carto-positron', hover_name='District'                                )
        st.plotly_chart(fig, size_container_width=True)