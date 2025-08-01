import streamlit as st
import pandas as pd
import altair as alt

st.title("Gráfico de datos")

# Cargar datos
df = pd.read_csv("datos.csv", parse_dates=["Fecha"])

st.subheader("Vista previa de los datos")
st.dataframe(df)

st.subheader("Gráfico de línea")
chart = alt.Chart(df).mark_line(point=True).encode(
    x="Fecha:T",
    y="Valor:Q",
    tooltip=["Fecha", "Valor"]
).interactive()

st.altair_chart(chart, use_container_width=True)
