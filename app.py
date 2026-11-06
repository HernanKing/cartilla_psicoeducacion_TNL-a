import streamlit as st
import os
import base64

st.set_page_config(layout="wide", page_title="Brochure Interactivo")

def get_image_base64(path):
    if os.path.exists(path):  # <--- Corregido el punto aquí
        with open(path, "rb") as image_file:
            encoded = base64.b64encode(image_file.read()).decode()
            return f"data:image/jpeg;base64,{encoded}"
    return ""

with open("index.html", "r", encoding="utf-8") as f:
    html_code = f.read()

for i in range(1, 34):
    img_path = f"images/page-{i}.jpg"
    img_base64 = get_image_base64(img_path)
    html_code = html_code.replace(f'images/page-{i}.jpg', img_base64)

st.components.v1.html(html_code, height=850, scrolling=True)
