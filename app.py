import streamlit as st
import os
import base64

st.set_page_config(layout="wide", page_title="Brochure Interactivo")

# Función para convertir las imágenes a Base64 y evitar errores de ruta en la nube
def get_image_base64(path):
    if os.path-exists(path):
        with open(path, "rb") as image_file:
            encoded = base64.b64encode(image_file.read()).decode()
            return f"data:image/jpeg;base64,{encoded}"
    return ""

# Leer el index.html
with open("index.html", "r", encoding="utf-8") as f:
    html_code = f.read()

# Reemplazar dinámicamente cada ruta de imagen por su versión en Base64 incrustada
for i in range(1, 34):
    img_path = f"images/page-{i}.jpg"
    img_base64 = get_image_base64(img_path)
    html_code = html_code.replace(f'images/page-{i}.jpg', img_base64)

# Renderizar el HTML completo dentro de Streamlit
st.components.v1.html(html_code, height=850, scrolling=True)
