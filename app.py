import streamlit as st
import requests
from google import genai

# Configuración Gemini
client = genai.Client(
    api_key="AQ.Ab8RN6KRtnwU8jcBpLOaxAQXPD7MtUJFHe2GVMQQ_NNJSD3oBg"
)

# Documento fuente
URL_DOCUMENTO = "https://raw.githubusercontent.com/sandragutierrezr/Educacion/refs/heads/main/Reglamento-Estudiantil-CUN.txt"

try:
    documento = requests.get(URL_DOCUMENTO, timeout=15).text[:15000]
except Exception as e:
    st.error(f"Error cargando documento: {e}")
    st.stop()

# ==========================
# INTERFAZ
# ==========================

st.title("🎓 Asistente Reglamento Estudiantil CUN")

st.write(
    "Realiza preguntas sobre el Reglamento Estudiantil de la CUN."
)

pregunta = st.text_input(
    "Escribe tu pregunta"
)

# ==========================
# CONSULTA
# ==========================

if st.button("Consultar"):

    if not pregunta.strip():
        st.warning("Por favor ingresa una pregunta.")
        st.stop()

    prompt = f"""
Eres un asistente educativo especializado en la Corporación Unificada Nacional de Educación Superior (CUN).

Responde únicamente utilizando la información contenida en el siguiente reglamento.

Si la respuesta no aparece en el documento, indica claramente que no fue encontrada.

DOCUMENTO:

{documento}

PREGUNTA:

{pregunta}
"""

    try:

        with st.spinner("Consultando reglamento..."):

            respuesta = client.models.generate_content(
                model="gemini-3.5-flash-lite",
                contents=prompt
            )

        st.subheader("📚 Respuesta")

        st.write(respuesta.text)

    except Exception as e:

        st.error(f"Error Gemini: {e}")
