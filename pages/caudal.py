import utilidades as util
import streamlit as st
from PIL import Image
import pandas as pd

util.generarMenu()

col1, col2, col3 = st.columns([0.5, 6, 0.5],
                                vertical_alignment='center')
with col2:
    # creamos un titulo y lo centramos
    st.title('Resultados de Caudal de rios en Antioquia')
    st.write("""
    El gráfico muestra las estaciones con mayor caudal promedio, lo que nos permite identificar aquellas con mayor potencial para la generación de energía hidroeléctrica. La estación de Puerto Berrio lidera con un caudal promedio de 2855 m³/s en el año 2022, seguida de cerca por las estaciones de Vigia del fuerte (2251 m³/s) y Nechi (2000 m³/s). Estas tres estaciones destacan significativamente por sus altos volúmenes de flujo, lo que las convierte en candidatas ideales para proyectos de generación energética.

    También es importante observar que existe una diferencia considerable entre las primeras posiciones y los municipios donde se presenta menos caudal. Esta disparidad sugiere que no todas las estaciones presentan el mismo potencial dada por la diversidad de afluentes presentes en antioquia de diverso tamaño, y podría ser necesario un análisis más detallado para determinar la estabilidad y variabilidad de los caudales.
    """)

    st.image('media/heatmap_caudal.jpeg', caption='Caudal promedio de rios en Antioquia', use_container_width=True)

    st.write("""
    Tendencias Temporales:

    Aunque se observan fluctuaciones anuales en los caudales, no se identifica una 
    tendencia clara de aumento o disminución sostenida en la mayoría de los municipios 
    analizados. Esto sugiere una estabilidad hidrológica relativa, aunque es esencial 
    considerar factores como el cambio climático y la variabilidad climática interanual 
    que podrían influir en el futuro.

    En conclusión, el gráfico proporciona una visión clara de la distribución del caudal 
    entre las estaciones con mayor flujo, lo que ayuda a priorizar posibles sitios para 
    el desarrollo de infraestructura hidroeléctrica. Un análisis adicional sobre la 
    consistencia temporal de estos caudales podría aportar información valiosa para 
    la toma de decisiones.
    """)
    
    st.image('media/anual-caudal-BI.png', caption='Caudal anual por municipio', use_container_width=True)
    st.write("""
    En el gráfico generado por un dashboard en Power BI, se puede observar el comportamiento de los 
    caudales através del tiempo, usando una escala de intensidad de color para representar 
    el caudal en cada municipio.\n
    No se observan tendencias de caudal por regiones específicas          
             """)
    
    st.image('media\diario caudal-BI.png', caption='Caudal promedio por día en cada municipio', use_container_width=True)   
    st.write("""
    En el gráfico generado por un dashboard en Power BI, se puede ver el caudal máximo por día del mes 
    en cada munipio, usando un gráfico de líneas por interpretar si existen patrones que se repitan 
    mensualmente.\n
    No se observan patrones claros en el comportamiento del caudal por día que sean comunes a todos 
    los municipios       
             
             """)