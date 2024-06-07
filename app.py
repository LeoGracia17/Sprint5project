import pandas as pd
import streamlit as st
import plotly.express as px

st.header('Datos de anuncios de ventas de coches')

car_data = pd.read_csv('/Users/leogracia17/TTdocs/GitHub/Sprint5project/vehicles_us.csv')
hist_button = st.button('Construir histograma')

if hist_button:
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
    fig = px.histogram(car_data, x = 'odometer')
    st.plotly_chart(fig, use_container_width= True)

disp_button = st.button('Construir diagrama de dispersión')

if disp_button:
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
    figu = px.scatter(car_data, x = 'odometer', y = 'price')
    st.plotly_chart(figu,use_container_width=True)

