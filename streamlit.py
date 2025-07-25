import streamlit as st
import plotly.express as px
import pandas as pd

# Data

mapeo = pd.read_csv("data/prd/mapeo.csv",sep=";")
st.write(mapeo.head())



# Establecer la configuración de la pantalla
st.set_page_config(
    page_title="Filtros",
    page_icon="🏠",
    layout="wide"
)



# Información
st.sidebar.title('Análisis')
st.sidebar.image('img/sports.png', width=150)
st.title('Recomendador de Jugadores')
st.write('Seleccione los filtros para ver los jugadores que cumplan ese criterio')


filtro_position = mapeo.position.unique().to_list()

position = st.selectbox("Elige tu opción:", filtro_position)

filtro_role = mapeo[mapeo["position"] == columna_seleccionada].role.unique().to_list()

role = st.selectbox("Elige tu opción:", filtro_role)

if role == "Extremo":
    st.write("No sos puto")
else:
    st.write("sos puto")