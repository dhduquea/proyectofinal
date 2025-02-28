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
    st.image('media/antioquia2.jpg', use_container_width=True)


col1, col2, col3 = st.columns([1, 2, 1],
                                  vertical_alignment='center')
with col2:
    st.write("""
    Antioquia, una región clave de Colombia, cuenta con una notable diversidad geográfica y climática que la hace ideal para el aprovechamiento de recursos naturales como la energía solar, la hidroelectricidad y la energía eólica. Sin embargo, la escasez de información consolidada y accesible sobre variables fundamentales como la radiación solar, los caudales de agua y la velocidad del viento limita la capacidad de planificación y toma de decisiones en sectores como la energía renovable, la agricultura y la gestión ambiental.

    Este proyecto tiene como objetivo cerrar esta brecha mediante la recopilación, limpieza, análisis y visualización de datos climáticos de fuentes confiables como IDEAM y Datos.gov. La meta es ofrecer una visión clara y detallada de estos indicadores en los municipios de Antioquia donde se disponga de datos.
    
    El objetivo de este análisis es evaluar el potencial de generación de energías renovables en el departamento de Antioquia, mediante un examen detallado de las bases de datos climáticos. Para ello, se recopila, limpia, analiza y visualiza información de fuentes confiables como el Instituto de Hidrología, Meteorología y Estudios Ambientales (IDEAM) y la plataforma Datos.gov. El propósito es recaudar información valiosa, analizarla, consolidarla y suministrarla para poder desarrollar insumos clave que permitan la toma de decisiones sobre la utilización y explotación de recursos naturales renovables en los diferentes municipios del departamento.
    
    Los resultados muestran que Antioquia posee un alto potencial para el desarrollo de energías renovables. Sin embargo, su aprovechamiento efectivo requiere estudios adicionales y la validación de los datos existentes. Se recomienda priorizar proyectos solares en municipios con alta radiación y evaluar la viabilidad de generación eólica en áreas con vientos constantes. Además, es esencial fortalecer la infraestructura de medición climática y mejorar el acceso a datos confiables para optimizar la planificación energética regional en aras de convertirnos en potencia energética renovable.
    """)