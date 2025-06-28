import streamlit as st
import plotly.express as px
import pandas as pd

st.title("Ejemplo de Radar Chart en Streamlit")

st.write("Este gráfico de radar muestra el rendimiento de un 'jugador' hipotético en varias métricas.")

# Datos de ejemplo para el radar chart
# Imagina estas métricas para un jugador de fútbol
data = {
    'Metric': ['Pases Completados', 'Regates Exitosos', 'Recuperaciones', 'Tiros al Arco', 'Asistencias'],
    'Player_A': [75, 60, 80, 50, 65],
    'Player_B': [85, 45, 70, 75, 55]
}
df = pd.DataFrame(data)

# Para un radar chart, a menudo se prefiere tener las métricas como columnas y los jugadores como filas.
# Hacemos un "melt" para reformar los datos.
df_melted = df.melt(id_vars=['Metric'], var_name='Player', value_name='Score')

# Creamos el radar chart con Plotly Express
# polar_theta es el eje angular (las métricas)
# polar_r es el eje radial (el puntaje)
fig = px.line_polar(df_melted, r='Score', theta='Metric', color='Player', line_close=True,
                    # Opciones adicionales para un mejor aspecto
                    range_r=[0,100],  # Establece el rango del eje radial de 0 a 100
                    template="plotly_white",
                    title="Comparación de Rendimiento de Jugadores")

# Actualizamos el layout para personalizar los ejes y la leyenda
fig.update_traces(fill='toself') # Rellena el área del radar
fig.update_layout(
    polar=dict(
        radialaxis=dict(
            visible=True,
            range=[0, 100]
        )
    ),
    showlegend=True
)

# Muestra el gráfico en Streamlit
st.plotly_chart(fig, use_container_width=True)

st.markdown("""
### ¿Qué puedes representar con un Radar Chart?
* **Rendimiento de Jugadores:** Habilidades (pases, tiros, defensa, físico)
* **Evaluación de Habilidades:** Competencias blandas o técnicas.
* **Análisis de Productos:** Características de diferentes productos.
* **Encuestas de Satisfacción:** Diferentes atributos calificados.
""")