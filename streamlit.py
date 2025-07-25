import streamlit as st
import plotly.express as px
import pandas as pd

# Data

mapeo = pd.read_csv("data/prd/mapeo.csv",encoding="utf-8")
st.write(mapeo.head())



# Establecer la configuración de la pantalla
st.set_page_config(
    page_title="Filtros",
    layout="wide"
)



# Información
st.sidebar.title('Análisis')
st.sidebar.image('img/sports.png', width=150)
st.title('Recomendador de Jugadores')
st.write('Seleccione los filtros para ver los jugadores que cumplan ese criterio')




position = st.selectbox("Elige tu opción:", mapeo["position"].unique().to_list())

role = st.selectbox("Elige tu opción:", mapeo[mapeo["position"] == position].role.unique().to_list())

if role == "Extremo":
    st.write("No sos puto")
else:
    st.write("Sos puto")