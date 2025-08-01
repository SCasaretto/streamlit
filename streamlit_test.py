import streamlit as st
import pandas as pd
import altair as alt

# Título
st.title("Visualización de datos desde CSV")

# Leer el archivo CSV
df = pd.read_csv("datos.csv", parse_dates=["Fecha"])

# Mostrar el dataframe
st.subheader("Datos cargados:")
st.dataframe(df)

# Gráfica con Altair
st.subheader("Gráfico de línea:")
chart = alt.Chart(df).mark_line(point=True).encode(
    x="Fecha:T",
    y="Valor:Q",
    tooltip=["Fecha", "Valor"]
).interactive()

st.altair_chart(chart, use_container_width=True)
