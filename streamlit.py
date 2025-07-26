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




st.session_state.position = st.selectbox("Elige tu opción:", mapeo["position"].unique().tolist(),index=None)

st.session_state.role = st.selectbox("Elige tu opción:", mapeo[mapeo["position"] == st.session_state.position].role.unique().tolist(),index=None)

if st.session_state.role == "Extremo":
    st.write("No sos puto")
else:
    st.write("Sos puto")