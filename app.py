import streamlit as st
import requests
from google import genai

# Configuración Gemini
client = genai.Client(
    api_key=st.secrets["GEMINI_API_KEY"]
)

# Documento fuente
URL_DOCUMENTO = "https://raw.githubusercontent.com/sandragutierrezr/Educacion/refs/heads/main/Reglamento-Estudiantil-CUN.txt"

documento = requests.get(URL_DOCUMENTO).text

# Interfaz
st.title("🎓 Asistente Reglamento Estudiantil CUN")

st.write(
    "Realiza preguntas sobre el Reglamento Estudiantil de la CUN."
)

pregunta = st.text_input(
    "Escribe tu pregunta"
)

if st.button("Consultar"):

    prompt = f"""
    Eres un asistente educativo especializado en la CUN.

    Responde únicamente con información basada en el siguiente reglamento:

    {documento}

    Pregunta:
    {pregunta}
    """

    respuesta = client.models.generate_content(
        model="gemini-3.5-flash-lite",
        contents=prompt
    )

    st.subheader("Respuesta")

    st.write(respuesta.text)
