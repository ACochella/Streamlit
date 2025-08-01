import pandas as pd
import streamlit as st
import plotly.graph_objects as go
import matplotlib.pyplot as plt # type: ignore
from math import pi
import plotly.express as px

def normalizar_por_90s(df):
    df = df.copy()
    columnas_a_normalizar = [
        col for col in df.columns
        if not col.endswith("_90s") and not col.startswith("perc_") and col != "90s" and col != "player" and not col.endswith("_%") and not col.endswith("_perc")
    ]

    # Creamos nuevas columnas normalizadas por '90s'
    for col in columnas_a_normalizar:
        nueva_col = col + "_90s"
        df[nueva_col] = round(df[col] / df["90s"],2)

    # Nos quedamos solo con columnas que terminan en '_90s' o empiezan con 'perc'
    columnas_finales = [col for col in df.columns if col.endswith("_90s") or col.startswith("perc_") or col.startswith("player")]
    df_filtrado = df[columnas_finales].copy()

    return df_filtrado

def radar_chart(df, jugadores, metricas, titulo):

    # Filtrar el DataFrame por jugadores y métricas
    df_filtrado = df[df["player"].isin(jugadores)][["player"] + metricas]

    # Ángulos del radar
    num_vars = len(metricas)
    angles = [n / float(num_vars) * 2 * pi for n in range(num_vars)]
    angles += angles[:1]  # Cierre del círculo

    # Crear gráfico
    fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))

    # Dibujar una línea para cada jugador
    for i, row in df_filtrado.iterrows():
        valores = row[metricas].tolist()
        valores += valores[:1]
        ax.plot(angles, valores, label=row["player"])
        ax.fill(angles, valores, alpha=0.1)

    # Estética
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels([m.replace("_", " ").capitalize() for m in metricas])
    ax.set_title(titulo, y=1.08)
    ax.legend(loc='upper right', bbox_to_anchor=(1.3, 1.1))

    # Mostrar en Streamlit
    st.pyplot(fig)


attack_metrics = ["goals_90s","assists_90s","goals_no_penalty_kicks_90s","xG_90s","xAG_90s","no_penalty_xG_90s","progressive_carries","progressive_passes","progressive_passes_received","shot_creating_actions_90s","play_passes_to_shot","goal_creating_actions_90s","play_passes_to_goal","offsides","passes_completed","perc_passes_completed","shoots_on_target_90s","short_passes_completed","perc_short_passes_completed","medium_passes_completed","perc_medium_passes_completed","key_passes","passes_into_final_third","passes_into_penalty_area","crosses_into_penalty_area","switches_passes","carries_into_ofe_third","carries_into_penalty_area","miscontrols","passes_received"]
defense_metrics = ["yellow_cards","red_cards","tackles_won","tackles_defensive_third","tackles_middle_third","tackles_offensive_third","dribblers_tackled","perc_dribblers_tackled","blocks","shots_blocked","passes_blocked","interceptions","tackles_and_interceptions","clearances","errors","second_yellow_card_expulsions","fouls_commited","aerial_duels_won","perc_aerial_duels_won","penalty_kicks_conceded"]
goalkeeper_metrics_1 = ["goals_against_90s","shoots_on_target_against","xG_post_shoot","xG_post_shoot_over_shoot_on_target","defensive_actions_outside_area_90s"]
goalkeeper_metrics_2 = ["saves_perc","clean_sheets_%","penalty_saved_perc","perc_goal_kicks","perc_crosses_stopped"]

df_attack = normalizar_por_90s(st.session_state.stats_players[(st.session_state.stats_players["classification"] == st.session_state.position + " " +st.session_state.role) & (st.session_state.stats_players["market_value_millions"].between(st.session_state.min_filtro, st.session_state.max_filtro))][["player","90s"] + attack_metrics])
df_defense = normalizar_por_90s(st.session_state.stats_players[(st.session_state.stats_players["classification"] == st.session_state.position + " " +st.session_state.role) & (st.session_state.stats_players["market_value_millions"].between(st.session_state.min_filtro, st.session_state.max_filtro))][["player","90s"] + defense_metrics])
df_gk_1 = normalizar_por_90s(st.session_state.stats_players[(st.session_state.stats_players["classification"] == st.session_state.position + " " +st.session_state.role) & (st.session_state.stats_players["market_value_millions"].between(st.session_state.min_filtro, st.session_state.max_filtro))][["player","90s"] + goalkeeper_metrics_1])
df_gk_2 = normalizar_por_90s(st.session_state.stats_players[(st.session_state.stats_players["classification"] == st.session_state.position + " " +st.session_state.role) & (st.session_state.stats_players["market_value_millions"].between(st.session_state.min_filtro, st.session_state.max_filtro))][["player","90s"] + goalkeeper_metrics_2])

attack_metrics_cleaned = ["goals_90s","assists_90s","goals_no_penalty_kicks_90s","xG_90s","xAG_90s","no_penalty_xG_90s","progressive_carries_90s","progressive_passes_90s","progressive_passes_received_90s","shot_creating_actions_90s","play_passes_to_shot_90s","goal_creating_actions_90s","play_passes_to_goal_90s","offsides_90s","passes_completed_90s","perc_passes_completed","shoots_on_target_90s","short_passes_completed_90s","perc_short_passes_completed","medium_passes_completed_90s","perc_medium_passes_completed","key_passes_90s","passes_into_final_third_90s","passes_into_penalty_area_90s","crosses_into_penalty_area_90s","switches_passes_90s","carries_into_ofe_third_90s","carries_into_penalty_area_90s","miscontrols_90s","passes_received_90s"]
defense_metrics_cleaned = ["yellow_cards_90s","red_cards_90s","tackles_won_90s","tackles_defensive_third_90s","tackles_middle_third_90s","tackles_offensive_third_90s","dribblers_tackled_90s","perc_dribblers_tackled","blocks_90s","shots_blocked_90s","passes_blocked_90s","interceptions_90s","tackles_and_interceptions_90s","clearances_90s","errors_90s","second_yellow_card_expulsions_90s","fouls_commited_90s","aerial_duels_won_90s","perc_aerial_duels_won","penalty_kicks_conceded_90s"]
goalkeeper_metrics_1_cleaned = ["goals_against_90s","shoots_on_target_against_90s","xG_post_shoot_90s","xG_post_shoot_over_shoot_on_target_90s","defensive_actions_outside_area_90s"]
goalkeeper_metrics_2_cleaned = ["saves_perc","clean_sheets_%","penalty_saved_perc","perc_goal_kicks","perc_crosses_stopped"]


jugadores = st.multiselect("Seleccioná jugadores", options=df_attack["player"].unique().tolist(), default=None, key="jugadores")

col1, col2 = st.columns(2)

with col1:
    if st.session_state.position != "Arquero":
        metricas1 = st.multiselect("Seleccioná métricas", options=attack_metrics_cleaned, default=None, key="metricas1")
        
        if not metricas1:
            st.info("Por favor seleccioná las métricas a considerar.")
        elif not jugadores:
            st.info("Selecciona los jugadores a comparar.")

        radar_chart(df_attack, jugadores, metricas1, "Comparativa de jugadores en ataque")
    else:
        metricas1 = st.multiselect("Seleccioná métricas", options=goalkeeper_metrics_1_cleaned, default=None, key="metricas1")
        
        if not metricas1:
            st.info("Por favor seleccioná las métricas a considerar.")
        elif not jugadores:
            st.info("Selecciona los jugadores a comparar.")

        radar_chart(df_gk_1, jugadores, metricas1, "Comparativa de arqueros")


with col2:
    if st.session_state.position != "Arquero":
        metricas2 = st.multiselect("Seleccioná métricas", options=defense_metrics_cleaned, default=None, key="metricas2")
        
        if not metricas2:
            st.info("Por favor seleccioná las métricas a considerar.")
        elif not jugadores:
            st.info("Selecciona los jugadores a comparar.")

        radar_chart(df_defense, jugadores, metricas2, "Comparativa de jugadores en defensa")
    else:
        metricas2 = st.multiselect("Seleccioná métricas", options=goalkeeper_metrics_2_cleaned, default=None, key="metricas2")
        
        if not metricas2:
            st.info("Por favor seleccioná las métricas a considerar.")
        elif not jugadores:
            st.info("Selecciona los jugadores a comparar.")

        radar_chart(df_gk_2, jugadores, metricas2, "Comparativa de arqueros")


historico_categorias = st.session_state.stats_players[st.session_state.stats_players["player"].isin(jugadores)][["player","classification"]]
historico_categorias["fecha"] = "202508"

st.write(historico_categorias)

fig = px.line(
    historico_categorias,
    x="fecha",
    y="classification",
    color="player",
    markers=True,
    line_group="player"
)

fig.update_layout(
    yaxis=dict(categoryorder='array', categoryarray=st.session_state.role),
    title="Evolución de rol por jugador",
    yaxis_title="Rol",
    xaxis_title="Fecha"
)

st.plotly_chart(fig)