import utilidades as util
import streamlit as st
from PIL import Image
import pandas as pd


st.set_page_config(page_title='Proyecto final',
                    layout='wide', 
                   initial_sidebar_state='expanded'
                   )
util.generarMenu()

col1, col2, col3 = st.columns([1, 0.7, 1],
                                  vertical_alignment='center')
with col2:
    st.image('media/Antioquia.jpg', use_container_width=True)

st.write("""
Antioquia, una región clave de Colombia, cuenta con una notable diversidad geográfica y climática que la hace ideal para el aprovechamiento de recursos naturales como la energía solar, la hidroelectricidad y la energía eólica. Sin embargo, la escasez de información consolidada y accesible sobre variables fundamentales como la radiación solar, los caudales de agua y la velocidad del viento limita la capacidad de planificación y toma de decisiones en sectores como la energía renovable, la agricultura y la gestión ambiental.

Este proyecto tiene como objetivo cerrar esta brecha mediante la recopilación, limpieza, análisis y visualización de datos climáticos de fuentes confiables como IDEAM y Datos.gov. La meta es ofrecer una visión clara y detallada de estos indicadores en los municipios de Antioquia donde se disponga de datos.
""")