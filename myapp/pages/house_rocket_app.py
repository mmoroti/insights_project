# =======================
#%% Import libraries
import pandas as pd
import streamlit as st
import numpy as np
import plotly.express as px
import seaborn as sns

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
data = pd.read_csv('..\kc_house_data.csv')
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

# ...
# %%
# Criando o gráfico de linha
pd.set_option('display.float_format', lambda x: f'{x:,.2f}')
data_sorted = data.groupby("zipcode").mean(["price"]).\
    sort_values(by='price',ascending=False).reset_index()\
    [["zipcode","price"]].astype(int)

fig = px.bar(data_sorted, x='zipcode', y='price', title='Preço médio por zip-code',
             category_orders=data_sorted.sort_values(by='price',ascending=False))
fig.update_xaxes(tickangle=90)
fig.update_xaxes(title_text='Código Postal')
fig.update_yaxes(title_text='Preço')

# Mostrando o gráfico no Streamlit
st.plotly_chart(fig)

# %%
# Criar o box plot para comparar as categorias
fig = px.box(data, x='view', y='price',
              title='Diferença de preço por tipo de vista')

# Rotular as categorias no eixo x
fig.update_xaxes(ticktext=['0', '1', '2', '3', '4'], tickvals=[0, 1])

# Mudar os nomes dos eixos
fig.update_xaxes(title_text='Tipo de vista')
fig.update_yaxes(title_text='Preço')

# Mostrar o box plot no Streamlit
st.plotly_chart(fig)