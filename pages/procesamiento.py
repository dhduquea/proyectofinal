import utilidades as util
import streamlit as st
from PIL import Image
import pandas as pd
from nbconvert.preprocessors import ExecutePreprocessor
import nbformat
import nbconvert

st.set_page_config(page_title='Procesamiento de los datos',
                    layout='wide', 
                   initial_sidebar_state='expanded')

util.generarMenu()

st.title("Procesamiento de datos")
st.write("En esta sección se muestra el proceso que se siguió para la limpieza de los datos para su posterior análisis")

with open("pages\Proyecto.html", "r", encoding="utf-8") as f:
    html_content = f.read()

st.components.v1.html(html_content, height=800, scrolling=True)

