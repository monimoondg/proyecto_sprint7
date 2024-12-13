import streamlit as st
import pandas as pd
import plotly.express as px

st.header('Relación de Vehiculos: Histogramas y Gráficos de dispersión')

car_data = pd.read_csv('vehicles_us.csv') # leer los datos
hist_button = st.button('Construir histograma') # crear un botón
        
if hist_button: # al hacer clic en el botón
         st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')# escribir un mensaje
         fig = px.histogram(car_data, x="odometer")
        # mostrar un gráfico Plotly interactivo
         st.plotly_chart(fig, use_container_width=True)

disp_button = st.button('Construir gráfico de dispersión') # crear un botón
        
if disp_button: # al hacer clic en el botón
         st.write('Creación de un gráfico de dispersión para el conjunto de datos de precios de venta de coches')# escribir un mensaje
         fig = px.scatter(car_data, x="odometer", y="price")
        # mostrar un gráfico Plotly interactivo
         st.plotly_chart(fig, use_container_width=True)