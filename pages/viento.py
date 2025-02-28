import utilidades as util
import streamlit as st
from PIL import Image

util.generarMenu()

col1, col2, col3 = st.columns([1, 5, 1],
                                  vertical_alignment='center')
with col2:
    st.title('Resultados de Viento en Antioquia')
    st.write("""
    El gráfico muestra las estaciones con mayor velocidad promedio del viento, lo que nos permite identificar aquellas con mayor potencial para la generación de energía eólica.
    """)
    st.image('media/barplot_viento.jpeg', caption='Velocidad promedio del viento en Antioquia', use_container_width=True)
    st.write("""
    Es importante observar que existe una diferencia considerable entre la primera posición y el resto de municipios, donde se presenta menor velocidad de viento. Esta disparidad sugiere la precensia de datos atipicos. Por lo que se decide realizar una limpieza de los datos para determinar la estabilidad y variabilidad de las velocidades de viento.
    """)
    st.image('media/dispersion_viento.jpeg', caption='Disperción de los datos de velocidad de viento', use_container_width=True)
    st.write("""
    En la anterior imagen se logra observar la presencia de datos atipicos en la velocidad del viento, por lo que se decide eliminar los datos que se encuentran por encima del rango de 50 m/s.
    Por lo que realizando un analisis rapido de los vecionos mas cercanos al municipio de Bello, se logra observar que estos datos no son normales. Por lo que se decide eliminar todos los valores por encima de 50 m/s.
             
    """)
    col1, col2, col3 = st.columns([2, 2, 2],
                                  vertical_alignment='center')
    with col2:
        st.image('media/analisis_dispersion_viento.jpeg', caption='Velocidad promedio del viento en Antioquia', use_container_width=True)

    st.write("""
    Una vez realizada limpieza, el grafico obtenido se observa a continuación, en el que se puede destacar los siguiente resultados.
             
    Municipios con Mayores Velocidades de Viento:
             
    Entrerríos y Medellín: Destacan Con velocidades entre 5 y 6 m/s, estos municipios presentan algunas condiciones favorables para proyectos eólicos. Velocidades de viento en este rango son estables para la operación eficiente de pequeños aerogeneradores, contribuyendo a una matriz energética diversificada y sostenible.
    Anorí, Bello, Amalfi y Jericó presentan una velocidad promedio de 4 a 5 m/s, lo que es relativamente medio y podría requerir una verificación adicional, por el momento son candidatos para la implementación a pequeña escala de proyectos de energía eólica.
    
    Municipios con Menores Velocidades de Viento:
             
    La mayoría de los municipios analizados registran velocidades inferiores a 4 m/s, lo que puede limitar la viabilidad económica de proyectos de energía eólica a gran escala. Sin embargo, podrían considerarse soluciones eólicas de pequeña escala para aplicaciones específicas, como el bombeo de agua o sistemas híbridos en zonas rurales.
    """)
    st.image('media/barplot_viento_trim.jpeg', caption='Velocidad promedio del viento en Antioquia', use_container_width=True)
    st.write("""
             \n \n
             """)
    st.image('media/anual-viento-BI.png', 
             caption='Velocidad máxima del viento anual en Antioquia', 
             use_container_width=True)
    st.write("""
            En el gráfico generado por un dashboard en Power BI, se puede observar el comportamiento anual
            de la velocidad del viento en cada municipio, usando una escala de intensidad de color en el 
            mapa para identificar patrones regionales de la medición.\n
            Se detectan varios picos anormales en la velocidad del viento, lo que sugiere la presencia de
            mediciones defectuosas en los sensores de las estaciones meteorológicas.
            """)
    st.image('media/diario-viento-BI.png',
            caption='Velocidad máxima del viento por día en cada municipio',
            use_container_width=True)
    st.write("""
            En el gráfico generado por un dashboard en Power BI, se puede observar el comportamiento de los
            valores de velocidad del viento máxima por día en cada municipio, usando un gráfico de líneas 
            para detectar patrones mensuales de comportamiento del viento.\n
            Se observan similitudes en algunas lineas de comportamiento pero no de manera significativa que 
            permita establecer un patrón regional.
             """)