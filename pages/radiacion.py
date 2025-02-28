import utilidades as util
import streamlit as st
from PIL import Image

util.generarMenu()
st.markdown("<h1 style='text-align: center;'>Radiación solar</h1>", unsafe_allow_html=True)


col1, col2, col3 = st.columns([0.5, 6, 0.5],
                                  vertical_alignment='center')
with col2:
    st.write("""
    La radiación solar es un factor determinante para la generación de energía solar fotovoltaica. En el gráfico se muestra la distribución de la radiación solar en los municipios de Antioquia. Los municipios de Medellín, Bello y Envigado presentan los mayores niveles de radiación solar en un periodo de 10 años, lo que los convierte en lugares ideales para la instalación de paneles solares. Estos municipios destacan por su alta exposición a la radiación solar, lo que les permite aprovechar al máximo la energía solar disponible.
    
    Por otro lado, los municipios de Yarumal, San Pedro de los Milagros y San Andrés de Cuerquia presentan los niveles más bajos de radiación solar en el mismo periodo. Estos municipios podrían no ser los más adecuados para la generación de energía solar, ya que su exposición a la radiación solar es limitada. Sin embargo, es importante tener en cuenta que la radiación solar puede variar considerablemente de un año a otro, por lo que es necesario realizar un análisis más detallado para determinar la viabilidad de la instalación de paneles solares en estos municipios.
    
    En resumen, el gráfico proporciona una visión general de la distribución de la radiación solar en los municipios de Antioquia, lo que ayuda a identificar los lugares con mayor potencial para la generación de energía solar fotovoltaica. Un análisis más detallado de la variabilidad de la radiación solar en estos municipios podría proporcionar información valiosa para la planificación de proyectos de energía solar.
    """)
    st.image("media/heatmap_rad_sol.jpeg", 
             caption='Municipos con mayor radiación solar en un periodo de 10 años',
             use_container_width=True)
    st.markdown("<h7 style='text-align: center;'>Municipios con Mayor Radiación Solar:</h2>", 
                unsafe_allow_html=True)
    st.write("""
    Santa Bárbara: Con un promedio de 378 Wh/m², este municipio, situado en la subregión del Suroeste, posee condiciones óptimas para la implementación de proyectos de energía solar fotovoltaica. La alta radiación solar puede ser aprovechada para generar electricidad sostenible y reducir la dependencia de fuentes fósiles.
    
    Santa Fe de Antioquia: Registrando 364 Wh/m², esta localidad, conocida por su clima cálido y seco, es ideal para instalaciones solares, tanto a nivel residencial como industrial. La promoción de energía solar en esta área podría impulsar el desarrollo económico local y atraer inversiones en tecnología limpia.
    Bello, Chigorodó, Turbo, y Yolombo también muestran altos indicies de radiación solar, aunque con una pequeña variabilidad, algo que también propiciaría el uso de la energía solar en los anteriores municipios.

    Municipios con Menor Radiación Solar:
             
    Medellín: Con 182 Wh/m², la capital del departamento muestra una radiación solar moderada, influenciada por su ubicación en un valle rodeado de montañas y una mayor nubosidad. Aunque la radiación es menor en comparación con otros municipios, aún es viable considerar proyectos solares, especialmente para autoconsumo en edificaciones.
    
    Observaciones Clave:
             
    La variación en la radiación solar entre municipios puede atribuirse a factores geográficos y climáticos, como la altitud, la latitud y la cobertura nubosa. Las áreas en altitudes más bajas y con menor nubosidad tienden a recibir mayor radiación solar, favoreciendo la generación de energía fotovoltaica.
    """)	
    
    st.image("media/anual-radsol-BI.png", 
             caption='Radiación solar anual por municipio',
             use_container_width=True)
    st.write("""
            En el gráfico generado por un dashboard en Power BI, se puede observar el comportamiento anual
            de la radiación solar en cada municipio, usando una escala de intensidad de color en el mapa
            del departamento.\n
            No se detectan patrones regionales de radiación solar anual
            """)
    
    st.image("media/diario-radsol-BI.png",
             caption='Radiación solar máxima por día en cada municipio',
             use_container_width=True)
    st.write("""
            En el gráfico generado por un dashboard en Power BI , se puede observar el comportamiento 
            de los valores de radiación solar máxima por día en cada municipio, usando un gráfico de líneas
            para interpretar si existen patrones que se repitan mensualmente.\n
            No se observan patrones claros en el comportamiento de la radiación solar por día que 
            sean comunes a todos los municipios.
            """)