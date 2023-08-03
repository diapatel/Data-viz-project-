import streamlit as st
import plotly.express as px
import numpy as np
import pandas as pd

st.set_page_config(layout='wide', page_title = 'Indian Census visualizer')
data= pd.read_csv('./india3.csv')
list_of_states = list(data['state'].unique())
list_of_states.insert(0,'Overall India')

st.sidebar.title('Visualizing India')
selected_state= st.sidebar.selectbox('Select a state', list_of_states)

parameter = st.sidebar.selectbox('Select a parameter', sorted(data.columns[6:]))
# if 'Household' not in parameter:
#     bubble = data['population']
# else:
#     bubble = data['households']
if selected_state == 'Overall India':
    filtered_data = data.copy()  # Use the entire dataset for overall India
else:
    filtered_data = data[data['state'] == selected_state]  # Filter data for the selected state

if 'Household' not in parameter:
    bubble = filtered_data['population']
    color = filtered_data[parameter]
else:
    bubble = filtered_data['households']
    color = filtered_data['households']
plot = st.sidebar.button('Plot a graph')

if plot:
    st.text('Size of the bubble represents population or number of households depending on the parameter')
    st.text('Color of the bubble represents the parameter')
    if selected_state == 'Overall India':
        #map for india
        fig = px.scatter_mapbox(data, lat='latitude', lon='longitude', size=bubble, color=parameter,
                                size_max=35, height=600, width=1000,
                                zoom=4, mapbox_style='carto-positron', hover_name='district'
                                )
        st.plotly_chart(fig, size_container_width=True)
    else:
        # map for the state
        state_df = data[data['state'] == selected_state]
        fig = px.scatter_mapbox(state_df, lat='latitude', lon='longitude', size=bubble, color=parameter,
                                size_max=35, height=600, width=1000,
                                zoom=5, mapbox_style='carto-positron' , hover_name='district'
                                )
        st.plotly_chart(fig, use_container_width=True)
        print(state_df)