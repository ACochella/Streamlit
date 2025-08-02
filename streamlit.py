import streamlit as st
import plotly.express as px
import pandas as pd
import base64
from pathlib import Path

# Ruta de la imagen relativa al archivo actual
image_path = Path(__file__).parent / "img" / "sports.png"

# Data

mapeo = pd.read_csv("data/prd/mapeo.csv",encoding="utf-8")


# Establecer la configuración de la pantalla
st.set_page_config(
    page_title="Inicio",
    layout="wide"
)

# Codificar la imagen en base64
with open(image_path, "rb") as img_file:
    encoded_image = base64.b64encode(img_file.read()).decode()

# Mostrar imagen fija abajo del sidebar con HTML
st.sidebar.markdown(
    f"""
    <style>
        .sidebar-bottom {{
            position: fixed;
            bottom: 20px;
            left: 20px;
        }}
    </style>
    <div class="sidebar-bottom">
        <img src="data:image/png;base64,{encoded_image}" width="100"/>
    </div>
    """,
    unsafe_allow_html=True
)

st.title('Recomendador de Jugadores')

st.markdown("#### Descubre, compara y analiza futbolistas con una visión integral basada en datos. Esta herramienta te permite identificar perfiles y roles para cada jugador,  además de evaluar métricas diferenciales que explican su rendimiento. Ideal para encontrar el tipo de jugador que tu club necesita incorporar.")
st.subheader("Filtros")
st.write('Seleccione los filtros para ver los jugadores que cumplan esos criterios')

position = st.selectbox("Elige la posición:", mapeo["position"].unique().tolist(),index=None)

st.session_state.position = position

role = st.selectbox("Elige el rol:", mapeo[mapeo["position"] == position].role.unique().tolist(),index=None)

st.session_state.role = role

valor_mercado = st.slider("Valor de mercado:", min_value=0, max_value=250,value=(0, 250))

# Extraer los límites del rango seleccionado por el usuario
st.session_state.min_filtro = valor_mercado[0]

st.session_state.max_filtro = valor_mercado[1]