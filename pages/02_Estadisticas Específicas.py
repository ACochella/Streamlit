import pandas as pd
import streamlit as st
import os
import matplotlib.pyplot as plt # type: ignore
import seaborn as sns # type: ignore

# ------------------------
# TITULOS
# ------------------------
st.title("Estadisticas de los jugadores en cada rol")
st.markdown("__________")



ruta_base = os.path.dirname(__file__)
ruta_csv = os.path.join(ruta_base, '..', 'data', 'prd', 'stats.csv')
stats_players = pd.read_csv(ruta_csv, encoding='utf-8')

st.session_state.stats_players = stats_players

if st.session_state.position == "Arquero":
    metrics = ["90s","passes_over_45m_completed","perc_passes_over_45m","defensive_actions_outside_area_90s","opponent_crosses_stopped","perc_crosses_stopped","goals_against_90s","xG_post_shoot","shoots_on_target_against","saves","clean_sheets","passes_completed","perc_passes_completed"]
    stats_role_tmp = stats_players[(stats_players["classification"] == st.session_state.position + " " +st.session_state.role) & (stats_players["market_value_millions"].between(st.session_state.min_filtro, st.session_state.max_filtro))][["player","team","nation","age","MP","starts","minutes","market_value_millions"] + metrics]
    
    stats_role_tmp["passes_over_45m_completed_90s"] = round(stats_role_tmp["passes_over_45m_completed"]/stats_role_tmp["90s"],2)
    stats_role_tmp["opponent_crosses_stopped_90s"] = round(stats_role_tmp["opponent_crosses_stopped"]/stats_role_tmp["90s"],2)
    stats_role_tmp["xG_post_shoot_90s"] = round(stats_role_tmp["xG_post_shoot"]/stats_role_tmp["90s"],2)
    stats_role_tmp["shoots_on_target_against_90s"] = round(stats_role_tmp["shoots_on_target_against"]/stats_role_tmp["90s"],2)
    stats_role_tmp["saves_90s"] = round(stats_role_tmp["saves"]/stats_role_tmp["90s"],2)
    stats_role_tmp["passes_completed_90s"] = round(stats_role_tmp["passes_completed"]/stats_role_tmp["90s"],2)

    stats_role = stats_role_tmp[["player","team","nation","age","MP","starts","minutes","market_value_millions","passes_over_45m_completed_90s","defensive_actions_outside_area_90s","opponent_crosses_stopped_90s","goals_against_90s","xG_post_shoot_90s","shoots_on_target_against_90s","saves_90s","clean_sheets","passes_completed_90s"]].set_index('player')
    st.write(stats_role)

elif st.session_state.position == "Defensor":
    metrics = ["90s","tackles_defensive_third","tackles_middle_third","tackles_offensive_third","dribblers_tackled","interceptions","errors","goals_90s","assists_90s","progressive_carries","progressive_passes","yellow_cards","red_cards","aerial_duels_won","crosses_into_penalty_area","fouls_commited","passes_completed","short_passes_completed","medium_passes_completed","passes_received"]
    stats_role_tmp = stats_players[(stats_players["classification"] == st.session_state.position + " " +st.session_state.role) & (stats_players["market_value_millions"].between(st.session_state.min_filtro, st.session_state.max_filtro))][["player","team","nation","age","MP","starts","minutes","market_value_millions"] + metrics]
    
    stats_role_tmp["tackles_defensive_third_90s"] = round(stats_role_tmp["tackles_defensive_third"]/stats_role_tmp["90s"],2)
    stats_role_tmp["tackles_middle_third_90s"] = round(stats_role_tmp["tackles_middle_third"]/stats_role_tmp["90s"],2)
    stats_role_tmp["tackles_offensive_third_90s"] = round(stats_role_tmp["tackles_offensive_third"]/stats_role_tmp["90s"],2)
    stats_role_tmp["dribblers_tackled_90s"] = round(stats_role_tmp["dribblers_tackled"]/stats_role_tmp["90s"],2)
    stats_role_tmp["interceptions_90s"] = round(stats_role_tmp["interceptions"]/stats_role_tmp["90s"],2)
    stats_role_tmp["errors_90s"] = round(stats_role_tmp["errors"]/stats_role_tmp["90s"],2)
    stats_role_tmp["progressive_carries_90s"] = round(stats_role_tmp["progressive_carries"]/stats_role_tmp["90s"],2)
    stats_role_tmp["progressive_passes_90s"] = round(stats_role_tmp["progressive_passes"]/stats_role_tmp["90s"],2)
    stats_role_tmp["yellow_cards_90s"] = round(stats_role_tmp["yellow_cards"]/stats_role_tmp["90s"],2)
    stats_role_tmp["red_cards_90s"] = round(stats_role_tmp["red_cards"]/stats_role_tmp["90s"],2)
    stats_role_tmp["aerial_duels_won_90s"] = round(stats_role_tmp["aerial_duels_won"]/stats_role_tmp["90s"],2)
    stats_role_tmp["crosses_into_penalty_area_90s"] = round(stats_role_tmp["crosses_into_penalty_area"]/stats_role_tmp["90s"],2)
    stats_role_tmp["fouls_commited_90s"] = round(stats_role_tmp["fouls_commited"]/stats_role_tmp["90s"],2)
    stats_role_tmp["passes_completed_90s"] = round(stats_role_tmp["passes_completed"]/stats_role_tmp["90s"],2)
    stats_role_tmp["short_passes_completed_90s"] = round(stats_role_tmp["short_passes_completed"]/stats_role_tmp["90s"],2)
    stats_role_tmp["medium_passes_completed_90s"] = round(stats_role_tmp["medium_passes_completed"]/stats_role_tmp["90s"],2)
    stats_role_tmp["passes_received_90s"] = round(stats_role_tmp["passes_received"]/stats_role_tmp["90s"],2)

    stats_role = stats_role_tmp[["player","team","nation","age","MP","starts","minutes","market_value_millions","tackles_defensive_third_90s","tackles_middle_third_90s","tackles_offensive_third_90s","dribblers_tackled_90s","interceptions_90s","errors_90s","goals_90s","assists_90s","progressive_carries_90s","progressive_passes_90s","yellow_cards_90s","red_cards_90s","aerial_duels_won_90s","crosses_into_penalty_area_90s","fouls_commited_90s","passes_completed_90s","short_passes_completed_90s","medium_passes_completed_90s","passes_received_90s"]].set_index('player')
    st.write(stats_role)

elif st.session_state.position == "Mediocampista":
    metrics = ["90s","interceptions","perc_dribblers_tackled","tackles_won","blocks","fouls_commited","passes_completed","perc_passes_completed","passes_into_penalty_area","passes_into_final_third","key_passes","xG_90s","xAG_90s","goals_90s","shoots_on_target_90s"]
    stats_role_tmp = stats_players[(stats_players["classification"] == st.session_state.position + " " +st.session_state.role) & (stats_players["market_value_millions"].between(st.session_state.min_filtro, st.session_state.max_filtro))][["player","team","nation","age","MP","starts","minutes","market_value_millions"] + metrics]
    
    stats_role_tmp["interceptions_90s"] = round(stats_role_tmp["interceptions"]/stats_role_tmp["90s"],2)
    stats_role_tmp["tackles_won_90s"] = round(stats_role_tmp["tackles_won"]/stats_role_tmp["90s"],2)
    stats_role_tmp["blocks_90s"] = round(stats_role_tmp["blocks"]/stats_role_tmp["90s"],2)
    stats_role_tmp["fouls_commited_90s"] = round(stats_role_tmp["fouls_commited"]/stats_role_tmp["90s"],2)
    stats_role_tmp["passes_completed_90s"] = round(stats_role_tmp["passes_completed"]/stats_role_tmp["90s"],2)
    stats_role_tmp["passes_into_final_third_90s"] = round(stats_role_tmp["passes_into_final_third"]/stats_role_tmp["90s"],2)
    stats_role_tmp["passes_into_penalty_area_90s"] = round(stats_role_tmp["passes_into_penalty_area"]/stats_role_tmp["90s"],2)
    stats_role_tmp["key_passes_90s"] = round(stats_role_tmp["key_passes"]/stats_role_tmp["90s"],2)

    stats_role = stats_role_tmp[["player","team","nation","age","MP","starts","minutes","market_value_millions","interceptions_90s","perc_dribblers_tackled","tackles_won_90s","blocks_90s","fouls_commited_90s","passes_completed_90s","perc_passes_completed","passes_into_penalty_area_90s","passes_into_final_third_90s","key_passes_90s","xG_90s","xAG_90s","goals_90s","shoots_on_target_90s"]].set_index('player')
    st.write(stats_role)

elif st.session_state.position == "Delantero":
    metrics = ["90s","shot_creating_actions_90s","goal_creating_actions_90s","offsides","aerial_duels_won","passes_into_final_third","passes_into_penalty_area","crosses_into_penalty_area","key_passes","carries_into_penalty_area","shoots_on_target_90s","goals_90s","assists_90s","xG_90s","xAG_90s","penalties_scored"]
    stats_role_tmp = stats_players[(stats_players["classification"] == st.session_state.position + " " +st.session_state.role) & (stats_players["market_value_millions"].between(st.session_state.min_filtro, st.session_state.max_filtro))][["player","team","nation","age","MP","starts","minutes","market_value_millions"] + metrics]
    
    stats_role_tmp["offsides_90s"] = round(stats_role_tmp["offsides"]/stats_role_tmp["90s"],2)
    stats_role_tmp["aerial_duels_won_90s"] = round(stats_role_tmp["aerial_duels_won"]/stats_role_tmp["90s"],2)
    stats_role_tmp["crosses_into_penalty_area_90s"] = round(stats_role_tmp["crosses_into_penalty_area"]/stats_role_tmp["90s"],2)
    stats_role_tmp["carries_into_penalty_area_90s"] = round(stats_role_tmp["carries_into_penalty_area"]/stats_role_tmp["90s"],2)
    stats_role_tmp["penalties_scored_90s"] = round(stats_role_tmp["penalties_scored"]/stats_role_tmp["90s"],2)
    stats_role_tmp["passes_into_final_third_90s"] = round(stats_role_tmp["passes_into_final_third"]/stats_role_tmp["90s"],2)
    stats_role_tmp["passes_into_penalty_area_90s"] = round(stats_role_tmp["passes_into_penalty_area"]/stats_role_tmp["90s"],2)
    stats_role_tmp["key_passes_90s"] = round(stats_role_tmp["key_passes"]/stats_role_tmp["90s"],2)

    stats_role = stats_role_tmp[["player","team","nation","age","MP","starts","minutes","market_value_millions","shot_creating_actions_90s","goal_creating_actions_90s","offsides_90s","aerial_duels_won_90s","passes_into_final_third_90s","passes_into_penalty_area_90s","crosses_into_penalty_area_90s","key_passes_90s","carries_into_penalty_area_90s","shoots_on_target_90s","goals_90s","assists_90s","xG_90s","xAG_90s","penalties_scored_90s"]].set_index('player')
    st.write(stats_role)

else:
    st.write("No se seleccionó tipo de jugador")

jugador = st.selectbox("Seleccione un jugador", stats_role_tmp["player"].unique().tolist(),index=None)

st.session_state.jugador = jugador

percentiles = stats_role.drop(["team","nation","age","MP","starts","minutes","market_value_millions"], axis=1)
percentiles = percentiles.rank(pct=True).multiply(100).round(1)

col1, col2 = st.columns(2) # Esto crea dos columnas de igual ancho

with col1:
    if jugador is not None:
        valores = percentiles.loc[[jugador]]

        metricas_posibles = percentiles.columns.tolist()
        metricas_destacadas = []

        for metrica in metricas_posibles:
            valor_jugador = valores[metrica].values[0]
            if valor_jugador >= 80:
                metricas_destacadas.append(metrica)
        # Gráfico solo si hay métricas destacadas
        if metricas_destacadas:
            fig, axes = plt.subplots(nrows=len(metricas_destacadas), figsize=(6, 4 * len(metricas_destacadas)))

            if len(metricas_destacadas) == 1:
                axes = [axes]  # para que se pueda iterar igual

            for ax, metrica in zip(axes, metricas_destacadas):
                sns.boxplot(data=stats_role, y=metrica, ax=ax, color='lightgray')
                ax.scatter(x=0, y=stats_role.loc[jugador, metrica], color='red', zorder=5)
                ax.set_title(f"Métrica destacada de {jugador}: {metrica.replace('_', ' ').capitalize()}")
                ax.legend()

            plt.tight_layout()
            st.pyplot(fig)
        else:
            st.info("Este jugador no supera el percentil 80 en ninguna métrica.")
    else:
        st.warning("Seleccioná un jugador para ver su gráfico de percentiles.")

with col2:
    if jugador is not None:

        # Gráfico para el jugador seleccionado
        valores = percentiles.loc[jugador]

        # Asignamos color según percentil
        colores = []
        for v in valores:
            if v < 40:
                colores.append('red')
            elif v <= 80:
                colores.append('gold')
            else:
                colores.append('green')

        # Matplotlib dentro de Streamlit
        fig, ax = plt.subplots(figsize=(8, 5))
        valores.plot(kind='bar', color=colores, edgecolor='black', ax=ax)
        ax.set_title(f"Percentiles de {jugador}")
        ax.set_ylabel("Percentil")
        ax.set_ylim(0, 100)
        ax.grid(axis='y', linestyle='--', alpha=0.7)
        ax.set_xticklabels(valores.index, rotation=90)

        # Etiquetas sobre las barras
        for i, v in enumerate(valores):
            ax.text(i, v + 2, f'{v}%', ha='center', fontweight='bold')

        st.pyplot(fig)
    else:
        st.warning("Seleccioná un jugador para ver su gráfico de percentiles.")




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