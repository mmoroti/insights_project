# Import libraries
import pandas as pd
import streamlit as st

st.set_page_config(layout='wide')
st.title('House Rocket Project')
st.markdown(' Welcome to House Rocket Data Analysis. Herein')

st.header('Load data')

# Functions
@st.cache( allow_output_mutation=True)
def get_data(path):
    # Lendo o arquivo
    data_all = pd.read_csv(path)
    # Transformando em date
    data_all['date'] = pd.to_datetime(data_all['date'], format='%Y-%m-%d')
    return data_all

df = get_data('kc_house_data.csv')
st.dataframe(df.head())