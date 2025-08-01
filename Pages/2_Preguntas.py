import streamlit as st
import pandas as pd
import altair as alt

import os
import requests
from dotenv import load_dotenv
from IPython.display import Markdown, display
from openai import OpenAI



system_prompt = "You are an assistant that analyzes the question given and respond in a shor answer. \
Respond in markdown."

# Título de la página
st.title("Modulo de Preguntas")

# Input de texto
texto_usuario = st.text_area("Pregunta:", height=150)

# Botón para procesar
if st.button("Enviar Pregunta"):   

    # Open and configure OpenAI client
    load_dotenv(override=True)
    api_key = os.getenv('OPENAI_API_KEY')

    if not api_key:
        print("No API key was found - please head over to the troubleshooting notebook in this folder to identify & fix!")
    else:
        print("API key found and looks good so far!")
    
    openai = OpenAI()

    # set the system prompt
    messages = [
    {"role": "system", "content": system_prompt},
    {"role": "user", "content": texto_usuario}
    ]

    # Call the OpenAI API
    response = openai.chat.completions.create(model="gpt-4o-mini", messages=messages)
    response_text = response.choices[0].message.content

    # Display the response
    st.subheader("Respuesta:")
    st.markdown(response_text)
