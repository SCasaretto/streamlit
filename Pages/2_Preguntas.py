import streamlit as st
import pandas as pd
import altair as alt

# Título de la página
st.title("Modulo de Preguntas")

# Input de texto
texto_usuario = st.text_area("Pregunta:", height=150)

# Botón para procesar
if st.button("Enviar Pregunta"):
    # Ejemplo de procesamiento (acá podés poner tu lógica)
    palabras = texto_usuario.split()
    cantidad_palabras = len(palabras)

    st.write("Texto original:")
    st.write(texto_usuario)

    st.write("Cantidad de palabras:", cantidad_palabras)
    
    # Ejemplo de gráfico: cantidad de letras por palabra
    

    df = pd.DataFrame({
        "Palabra": palabras,
        "Largo": [len(p) for p in palabras]
    })

    chart = alt.Chart(df).mark_bar().encode(
        x='Palabra',
        y='Largo'
    ).properties(title="Largo de cada palabra")

    st.altair_chart(chart, use_container_width=True)
