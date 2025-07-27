import pandas as pd
import streamlit as st
import os

# ------------------------
# TITULOS
# ------------------------
st.title("🔎 Buscando grupos de equipos")
st.markdown("__________")



ruta_base = os.path.dirname(__file__)
ruta_csv = os.path.join(ruta_base, '..', 'data', 'prd', 'stats.csv')
stats_players = pd.read_csv(ruta_csv, encoding='utf-8')

st.write(st.session_state.position + " " +st.session_state.role)

stats_role = stats_players[stats_players["classification"] == st.session_state.position + " " +st.session_state.role]
st.write(stats_role)

# ------------------------
# GENERACION DE FILTROS
## 1. Selección de competicion (variable Competition)
# ------------------------
#with st.sidebar.expander("Selección de la muestra"):
#    # Filtro de ligas
#    comp = df_clubes['Competition'].unique().tolist()
#    comp_selected = st.multiselect(
#        'Competiciones', options = comp, 
#        default = ['La Liga']) # ['La Liga', 'Premier League']
#    df_full = df_clubes[df_clubes.Competition.isin(comp_selected)]
#    # cambio en algun nombre
#    df_full.loc[df_full.Squad == 'Casa Pia', 'Squad'] = 'Casa Pia AC'
#    df_full.loc[df_full.Squad == 'Vizela', 'Squad'] = 'FC Vizela'
#    st.info("Número de clubes: {n}".format(n=df_full.shape[0]))