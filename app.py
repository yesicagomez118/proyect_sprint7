import streamlit as st
import pandas as pd
import plotly.express as px
st.markdown("""
<style>
.stApp {
    background-color: gray !important;
}
.main .block-container {
    background-color: gray !important;
}
div[data-testid="stAppViewContainer"] {
    background-color: gray !important;
}
</style>
""", unsafe_allow_html=True)
st.header('ESTADISTICAS DE VEHICULOS EN ESTADOS UNIDOS')
st.image('https://images.unsplash.com/photo-1502877338535-766e1452684a?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1470&q=80', use_container_width=True)   

car_data = pd.read_csv('vehicles_us.csv')

hist_button = st.button('Construir histograma para kilometraje') # crear un botón
     
if hist_button: # al hacer clic en el botón
         # escribir un mensaje
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
         
         # crear un histograma
    fig = px.histogram(car_data, x="odometer")
     
         # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)
scatter_button = st.button('Construir gráfico de dispersión para kilometraje') # crear un botón
if scatter_button: # al hacer clic en el botón
         # escribir un mensaje
    st.write('Creación de un gráfico de dispersión para el conjunto de datos de anuncios de venta de coches')
         
         # crear un histograma
    fig2 = px.scatter(car_data, x="odometer", y="price")
     
         # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig2, use_container_width=True) 
hist_button2 = st.button('Construir histograma para modelo') # crear un botón
if hist_button2: # al hacer clic en el botón
         # escribir un mensaje
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
         
         # crear un histograma
    fig3 = px.histogram(car_data, x="model_year")
     
         # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig3, use_container_width=True)    
    
     