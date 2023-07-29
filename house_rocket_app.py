# =======================
#%% Import libraries
import pandas as pd
import streamlit as st
import numpy as np
import plotly.express as px

# =======================
#%% Functions
st.set_page_config(page_title="Plotting Demo", page_icon="📈", layout='wide')
st.title('House Rocket Project')
st.markdown(' Welcome to House Rocket Data Analysis.')

@st.cache( allow_output_mutation=True)
def get_data(path):
    # Lendo o arquivo
    data_all = pd.read_csv(path)
    # Transformando em date
    data_all['date'] = pd.to_datetime(data_all['date'], format='%Y%m%dT%H%M%S')
    return data_all

# =======================
#%% Extract
data = pd.read_csv('kc_house_data.csv')
data['date'] = pd.to_datetime(data['date'], format='%Y%m%dT%H%M%S')

# =======================
#%%Transformation
# Add new features
data['price_m2'] = data['price']/(data['sqft_lot']/10.764)

# Add filters
# columns filter
f_attributes = st.sidebar.multiselect('Select columns', data.columns )
# rows filter
f_zipcode = st.sidebar.multiselect('Select zipcode', 
                    data['zipcode'].sort_values(ascending=True).unique())
#bedrooms = st.sidebar.multiselect('Number of bedrooms', 
             #data['bedrooms'].sort_values(ascending=True).unique())
# Preparing dataset with filters

st.header('Data Overview')
if (f_zipcode != []) & (f_attributes != []):
    filter_data = data.loc[data['zipcode'].isin(f_zipcode), f_attributes]
elif (f_zipcode == []) & (f_attributes != []):
    filter_data = data.loc[:, f_attributes]
elif (f_zipcode != []) & (f_attributes == []):
    filter_data = data.loc[data['zipcode'].isin(f_zipcode), :]
else:
    filter_data = data.copy()
st.write(filter_data)

#map filter
price_min = int(data['price'].min())
price_max = int(data['price'].max())
price_mean = int(data['price'].mean())
#st.button("Re-run")

### Load
# Map 
#%%
st.header('# ======================= #')
st.header('House Rocket Map')
is_check = st.checkbox('Display map') 
price_slider = st.slider('Price range', price_min,price_max,price_mean)

if is_check:
    #select rows
    houses = data[data['price'] < price_slider]
    fig = px.scatter_mapbox( houses,
                        lat = 'lat',
                        lon = 'long',
                        size = 'price',
                        color = 'zipcode',
                        size_max = 20,
                        zoom = 10)

    fig.update_layout (mapbox_style = 'open-street-map')
    fig.update_layout( height=600, margin= {'r': 0, 'l':0, 'b':0, 't':0} )
    st.plotly_chart(fig)
# %%
# ...
# ...
