import pandas as pd
import streamlit as st
import plotly.graph_objects as go
import matplotlib.pyplot as plt # type: ignore
from math import pi

def normalizar_por_90s(df):
    df = df.copy()
    columnas_a_normalizar = [
        col for col in df.columns
        if not col.endswith("_90s") and not col.startswith("perc_") and col != "90s" and col != "player"
    ]

    # Creamos nuevas columnas normalizadas por '90s'
    for col in columnas_a_normalizar:
        nueva_col = col + "_90s"
        df[nueva_col] = round(df[col] / df["90s"],2)

    # Nos quedamos solo con columnas que terminan en '_90s' o empiezan con 'perc'
    columnas_finales = [col for col in df.columns if col.endswith("_90s") or col.startswith("perc_") or col.startswith("player")]
    df_filtrado = df[columnas_finales].copy()

    return df_filtrado


attack_metrics = ["goals_90s","assists_90s","goals_no_penalty_kicks_90s","xG_90s","xAG_90s","no_penalty_xG_90s","progressive_carries","progressive_passes","progressive_passes_received","shot_creating_actions_90s","play_passes_to_shot","goal_creating_actions_90s","play_passes_to_goal","offsides","passes_completed","perc_passes_completed","shoots_on_target_90s","short_passes_completed","perc_short_passes_completed","medium_passes_completed","perc_medium_passes_completed","key_passes","passes_into_final_third","passes_into_penalty_area","crosses_into_penalty_area","switches_passes","carries_into_ofe_third","carries_into_penalty_area","miscontrols","passes_received"]
defense_metrics = ["yellow_cards","red_cards","tackles_won","tackles_defensive_third","tackles_middle_third","tackles_offensive_third","dribblers_tackled","perc_dribblers_tackled","blocks","shots_blocked","passes_blocked","interceptions","tackles_and_interceptions","clearances","errors","second_yellow_card_expulsions","fouls_commited","aerial_duels_won","perc_aerial_duels_won","penalty_kicks_conceded"]
goalkeeper_metrics_1 = ["goals_against_90s","shoots_on_target_against","xG_post_shoot","xG_post_shoot_over_shoot_on_target","defensive_actions_outside_area_90s"]
goalkeeper_metrics_2 = ["saves_perc","clean_sheets_%","penalty_saved_perc","perc_goal_kicks","perc_crosses_stopped"]

df_attack = normalizar_por_90s(st.session_state.stats_players[(st.session_state.stats_players["classification"] == st.session_state.position + " " +st.session_state.role) & (st.session_state.stats_players["market_value_millions"].between(st.session_state.min_filtro, st.session_state.max_filtro))][["player","90s"] + attack_metrics])
df_defense = normalizar_por_90s(st.session_state.stats_players[(st.session_state.stats_players["classification"] == st.session_state.position + " " +st.session_state.role) & (st.session_state.stats_players["market_value_millions"].between(st.session_state.min_filtro, st.session_state.max_filtro))][["player","90s"] + defense_metrics])
df_gk_1 = normalizar_por_90s(st.session_state.stats_players[(st.session_state.stats_players["classification"] == st.session_state.position + " " +st.session_state.role) & (st.session_state.stats_players["market_value_millions"].between(st.session_state.min_filtro, st.session_state.max_filtro))][["player","90s"] + goalkeeper_metrics_1])
df_gk_2 = normalizar_por_90s(st.session_state.stats_players[(st.session_state.stats_players["classification"] == st.session_state.position + " " +st.session_state.role) & (st.session_state.stats_players["market_value_millions"].between(st.session_state.min_filtro, st.session_state.max_filtro))][["player","90s"] + goalkeeper_metrics_2])




col1, col2 = st.columns(2)

with col1:
    jugadores1 = st.multiselect("Seleccioná métricas", options=df_attack["player"].unique().tolist(), default=None, key="jugadores1")
    metricas1 = st.multiselect("Seleccioná métricas", options=attack_metrics, default=None, key="metricas1")
    
    if not metricas1:
        st.info("Por favor seleccioná las métricas a considerar.")
    elif not jugadores1:
        st.info("Selecciona los jugadores a comparar.")
    else:
        jugador = 'Jugador 1'
        valores = df_attack.loc[jugadores1, metricas1]
        
        #for metrica in metricas:
        #    min_val = df[metrica].min()
        #    max_val = df[metrica].max()
        #    data_norm[metrica] = 100 * (data[metrica] - min_val) / (max_val - min_val)

        num_vars = len(metricas1)
        angles = [n / float(num_vars) * 2 * pi for n in range(num_vars)]
        angles += angles[:1]

        fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))
        
        for i, row in valores.iterrows():
            valores = row[metricas1].tolist()
            valores += valores[:1]
            ax.plot(angles, valores, label=row["player"])
            ax.fill(angles, valores, alpha=0.1)

        ax.set_xticks(angles[:-1])
        ax.set_xticklabels([m.replace("_", " ").capitalize() for m in metricas1])
        ax.set_title("Comparativa métricas de ataque", y=1.08)
        ax.legend(loc='upper right', bbox_to_anchor=(1.3, 1.1))

        st.pyplot(fig)

# ----- COLUMNA 2 -----
with col2:
    st.subheader("Jugador 2")
    metricas2 = st.multiselect("Seleccioná métricas", options=defense_metrics, default=None, key="metricas2")
    
    if not metricas2:
        st.info("Por favor seleccioná las métricas a considerar.")
    else:
        jugador = 'Jugador 2'
        valores = df_defense.loc[jugador, metricas2].values.tolist()
        
        fig = go.Figure()
        fig.add_trace(go.Scatterpolar(
            r=valores,
            theta=[m.replace('_', ' ').capitalize() for m in metricas2],
            fill='toself',
            name=jugador
        ))
        fig.update_layout(
            polar=dict(radialaxis=dict(visible=True)),
            showlegend=True
        )
        st.plotly_chart(fig, use_container_width=True)