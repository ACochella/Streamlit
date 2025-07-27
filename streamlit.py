import streamlit as st
import plotly.express as px
import pandas as pd

# Data

mapeo = pd.read_csv("data/prd/mapeo.csv",encoding="utf-8")


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

position = st.selectbox("Elige la posición:", mapeo["position"].unique().tolist(),index=None)

st.session_state.position = position

role = st.selectbox("Elige el rol:", mapeo[mapeo["position"] == position].role.unique().tolist(),index=None)

st.session_state.role = role

valor_mercado = st.slider("Valor de mercado:", min_value=0, max_value=250,value=(0, 250))

# Extraer los límites del rango seleccionado por el usuario
st.session_state.min_filtro = valor_mercado[0]

st.session_state.max_filtro = valor_mercado[1]