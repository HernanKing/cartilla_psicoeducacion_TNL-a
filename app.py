import streamlit as st
import os

# Configuración de la página para que ocupe todo el ancho
st.set_page_config(layout="wide", page_title="Brochure Interactivo")

# Leer el archivo index.html local
with open("index.html", "r", encoding="utf-8") as f:
    html_code = f.read()

# Mostrar el HTML dentro de la aplicación de Streamlit
st.components.v1.html(html_code, height=850, scrolling=True)
